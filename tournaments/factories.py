from __future__ import annotations
from typing import TYPE_CHECKING

from players.factories import make_player
from shops.factories import make_shop
from tournaments import models

if TYPE_CHECKING:
    from players.models import Player
    from shops.models import Shop


def make_tournament(
    number: int = 1,
    description: str = "Test Tournament",
    shop: Shop | None = None,
    season: models.Season | None = None,
) -> models.Tournament:
    if shop is None:
        shop = make_shop()
    if season is None:
        season = make_season()

    return models.Tournament.objects.create(
        number=number,
        description=description,
        shop=shop,
        season=season,
    )


def make_season(name: str = "Test Season", point_version: str = "v1") -> models.Season:
    return models.Season.objects.create(
        name=name,
        point_version=point_version,
    )


def make_stading(tournament: models.Tournament | None = None) -> models.Standing:
    return models.Standing.objects.create(
        tournament=tournament if tournament is not None else make_tournament(),
    )


def make_participation(
    player: Player | None = None,
    swiss_win: int = 3,
    final_standing: int = 1,
    standing: models.Standing | None = None,
) -> models.Participation:
    if player is None:
        player = make_player()

    if standing is None:
        standing = make_stading()

    return models.Participation.objects.create(
        player=player,
        swiss_win=swiss_win,
        final_standing=final_standing,
        standing=standing,
    )


def make_lost(
    loser: Player,
    winner: Player | None = None,
    is_double_loss: bool = False,
    standing: models.Standing | None = None,
) -> models.MatchResult:
    if winner is None:
        winner = make_player()
    return models.MatchResult.objects.create(
        winner=winner,
        loser=loser,
        is_double_loss=is_double_loss,
        standing=standing if standing is not None else make_stading(),
    )


def make_win(
    winner: Player,
    loser: Player | None = None,
    is_double_loss: bool = False,
    standing: models.Standing | None = None,
) -> models.MatchResult:
    if loser is None:
        loser = make_player()
    return models.MatchResult.objects.create(
        winner=winner,
        loser=loser,
        is_double_loss=is_double_loss,
        standing=standing if standing is not None else make_stading(),
    )
