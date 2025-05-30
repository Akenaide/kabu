from typing import List
from django.db.models import Q
from django.db.models.functions import Lower
from django.shortcuts import get_object_or_404, render

from players import models
from players.dataclasses import PlayerStatsVsPlayer
from tournaments.models import MatchResult
# Create your views here.


def stats_pvp(player_a: models.Player, player_b: models.Player) -> PlayerStatsVsPlayer:
    win = 0
    total = 0
    total_qs: List[MatchResult] = MatchResult.objects.filter(
        Q(winner=player_a, loser=player_b) | Q(winner=player_b, loser=player_a),
    )
    for match in total_qs:
        if match.winner_id == player_a.id:
            win += 1
        total += 1
    wr = win / total * 100 if total else None
    return PlayerStatsVsPlayer(val=wr, player=player_b)


def detail_player(request, pk):
    player = get_object_or_404(models.Player.objects.with_winrate(), pk=pk)
    context = {
        "player": player,
    }
    # TODO: matchs_won and matchs_lost do not consider `is_double_loss` so the page can be incorrect
    return render(
        request=request,
        context=context,
        template_name="detail_player.html",
    )


def list_players(request):
    context = {
        "players": models.Player.objects.all().order_by(Lower("identifier")),
    }
    return render(
        request=request,
        context=context,
        template_name="list_players.html",
    )


def all_stats(request):
    players_with_global_stats = (
        models.Player.objects.with_winrate().order_by().exclude(winrate=None)
    )

    stats_table = []
    for row in players_with_global_stats:
        row_data: List[PlayerStatsVsPlayer] = []
        row_data.append(PlayerStatsVsPlayer(str(row), player=row))
        for col in players_with_global_stats:
            row_data.append(stats_pvp(row, col))
        stats_table.append(row_data)

    context = {
        "players": players_with_global_stats,
        "stats_table": stats_table,
    }

    return render(
        request=request,
        context=context,
        template_name="all_stats.html",
    )
