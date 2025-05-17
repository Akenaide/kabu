from django.test import TestCase

from players import models
from players.factories import make_player
from tournaments.factories import make_lost, make_win

# Create your tests here.


class PlayerTest(TestCase):
    def test_with_winrate_queryset(self):
        winner = make_player()
        make_win(winner=winner)
        make_lost(loser=winner)
        make_lost(loser=winner)
        annotation = models.Player.objects.filter(pk=winner.pk).with_winrate().first()
        self.assertAlmostEqual(annotation.winrate, 33.33, places=2)
