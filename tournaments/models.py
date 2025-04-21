import datetime
from typing import override
from django.db import models

# Create your models here.


class Season(models.Model):
    name = models.CharField()
    point_version = models.CharField(default="v1")

    @override
    def __str__(self):
        return f"{self.pk} - {self.name}"


class Tournament(models.Model):
    number = models.IntegerField()
    date = models.DateField(default=datetime.date.today)
    description = models.TextField(blank=True)
    season = models.ForeignKey("tournaments.Season", on_delete=models.PROTECT)
    shop = models.ForeignKey("shops.Shop", on_delete=models.PROTECT)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["number", "season", "shop"],
                name="only_one_number_by_shop_by_season",
            ),
        ]

    @override
    def __str__(self):
        return f"{self.pk} - Tournament {self.number} shop {self.shop.name}"


class Participation(models.Model):
    player = models.ForeignKey("players.Player", on_delete=models.PROTECT)
    swiss_win = models.PositiveIntegerField()
    final_standing = models.PositiveIntegerField()
    standing = models.ForeignKey("tournaments.Standing", on_delete=models.PROTECT)

    class Meta:
        ordering = ["final_standing"]

    @property
    def calculate_point(self):
        swiss_points = 3 * self.swiss_win
        total_participant = self.standing.participation_set.count()
        total_participant = self.standing.participation_set.count()

        if total_participant >= 16:
            points = [6, 4, 2, 2, 1, 1, 1, 1]
        elif total_participant >= 9:
            points = [4, 2, 1, 1]
        else:
            points = [2, 1]

        if self.final_standing <= len(points):
            standing_points = points[self.final_standing - 1]
        else:
            standing_points = 0

        total_points = (
            swiss_points
            + standing_points
            + (total_participant - self.final_standing) / 10
        )
        return max(total_points, 1)


class Standing(models.Model):
    tournament = models.OneToOneField(
        "tournaments.Tournament",
        on_delete=models.PROTECT,
    )

    @override
    def __str__(self):
        return f"{self.pk} - for tournament {self.tournament.pk}"
