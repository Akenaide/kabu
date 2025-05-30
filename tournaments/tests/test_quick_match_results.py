from django.test import TestCase, Client
from django.urls import reverse
from players.models import Player
from tournaments.models import Season, Tournament, Standing, MatchResult
from shops.models import Shop
from datetime import date


class QuickMatchResultsTestCase(TestCase):
    def setUp(self):
        # Create required objects for testing
        self.client = Client()

        # Create test data
        self.season = Season.objects.create(name="Test Season")
        self.shop = Shop.objects.create(name="Test Shop")
        self.tournament = Tournament.objects.create(
            number=1,
            season=self.season,
            shop=self.shop,
            date=date.today(),
        )
        self.standing = Standing.objects.create(tournament=self.tournament)

        # Create players
        self.player1 = Player.objects.create(identifier="Player1")
        self.player2 = Player.objects.create(identifier="Player2")

    def test_quick_match_results_view_get(self):
        """Test the quick match results view GET request"""
        url = reverse("quick-match-results", args=[self.standing.pk])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "quick_match_results.html")

    def test_quick_match_results_with_default_player(self):
        """Test the quick match results view with a default player"""
        url = f"{reverse('quick-match-results', args=[self.standing.pk])}?player_id={self.player1.pk}"
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["default_player"], self.player1)

    def test_quick_match_results_post_win(self):
        """Test posting a win result"""
        url = f"{reverse('quick-match-results', args=[self.standing.pk])}?player_id={self.player1.pk}"
        data = {
            "opponent": self.player2.pk,
            "outcome": "win",
        }

        response = self.client.post(url, data)

        # Check redirect
        self.assertEqual(response.status_code, 302)

        # Check match result was created
        match = MatchResult.objects.first()
        self.assertIsNotNone(match)
        self.assertEqual(match.winner, self.player1)
        self.assertEqual(match.loser, self.player2)
        self.assertFalse(match.is_double_loss)

    def test_quick_match_results_post_loss(self):
        """Test posting a loss result"""
        url = f"{reverse('quick-match-results', args=[self.standing.pk])}?player_id={self.player1.pk}"
        data = {
            "opponent": self.player2.pk,
            "outcome": "loss",
        }

        self.client.post(url, data)

        # Check match result was created
        match = MatchResult.objects.first()
        self.assertIsNotNone(match)
        self.assertEqual(match.winner, self.player2)
        self.assertEqual(match.loser, self.player1)
        self.assertFalse(match.is_double_loss)

    def test_quick_match_results_post_double_loss(self):
        """Test posting a double loss result"""
        url = f"{reverse('quick-match-results', args=[self.standing.pk])}?player_id={self.player1.pk}"
        data = {
            "opponent": self.player2.pk,
            "outcome": "double_loss",
        }

        self.client.post(url, data)

        # Check match result was created
        match = MatchResult.objects.first()
        self.assertIsNotNone(match)
        self.assertEqual(match.winner, self.player1)
        self.assertEqual(match.loser, self.player2)
        self.assertTrue(match.is_double_loss)

    def test_quick_match_results_missing_data(self):
        """Test posting with missing data"""
        url = f"{reverse('quick-match-results', args=[self.standing.pk])}?player_id={self.player1.pk}"
        data = {
            "opponent": "",
            "outcome": "win",
        }

        response = self.client.post(url, data)

        # Should not redirect, should return the form with an error
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Please select all required fields")

        # No match should be created
        self.assertEqual(MatchResult.objects.count(), 0)
