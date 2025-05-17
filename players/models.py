from django.db import models
from django.db.models.aggregates import Count
from django.db.models.functions import Round
from django.db.models.query import Cast

# Create your models here.


class PlayersManager(models.Manager):
    pass


class PlayersQuerySet(models.QuerySet):
    def with_winrate(self):
        return self.annotate(
            won_count=Count(
                "matchs_won",
                filter=models.Q(matchs_won__is_double_loss=False),
                distinct=True,
            ),
            matchs_count=Count(
                "matchs_won",
                filter=models.Q(matchs_won__isnull=False),
                distinct=True,
            )
            + Count(
                "matchs_lost",
                filter=models.Q(matchs_lost__isnull=False),
                distinct=True,
            ),
            winrate=Round(
                Cast(
                    models.F("won_count"),
                    output_field=models.FloatField(),
                )
                / models.F("matchs_count")
                * 100,
                precision=2,
            ),
        )


class Player(models.Model):
    identifier = models.CharField(unique=True)
    verbose_name = models.CharField(blank=True)

    objects = PlayersManager.from_queryset(PlayersQuerySet)()

    def __str__(self):
        return f"{self.pk} - {self.identifier}"
