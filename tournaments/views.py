from typing import List
from django.template.response import SimpleTemplateResponse, TemplateResponse
from django.shortcuts import get_object_or_404, redirect, reverse

from players.models import Player
from tournaments import forms, models
# Create your views here.


def list_tournaments(request):
    context = {
        "tournaments": models.Tournament.objects.all(),
    }
    return SimpleTemplateResponse(
        "list_tournaments.html",
        context=context,
    )


def list_seasons(request):
    context = {
        "seasons": models.Season.objects.all(),
    }
    return SimpleTemplateResponse(
        "list_seasons.html",
        context=context,
    )


def detail_season(request, pk):
    season = get_object_or_404(models.Season, pk=pk)
    context = {
        "season": season,
    }
    return SimpleTemplateResponse(
        "detail_season.html",
        context=context,
    )


def match_results(request, pk):
    standing = get_object_or_404(models.Standing, pk=pk)
    # find previous and next
    standing_ids: List[int] = list(
        models.Standing.objects.order_by("pk").values_list("pk", flat=True),
    )
    standing_index = standing_ids.index(standing.pk)
    try:
        previous_standing = standing_ids[standing_index - 1]
    except IndexError:
        previous_standing = None

    try:
        next_standing = standing_ids[standing_index + 1]
    except IndexError:
        next_standing = None

    context = {
        "standing": standing,
        "match_results": standing.matchresult_set.all(),
        "form": forms.MatchResultForm(players=Player.objects.all()),
        "previous_standing": previous_standing,
        "next_standing": next_standing,
    }

    return TemplateResponse(
        request=request,
        template="match_results.html",
        context=context,
    )


def add_match_results(request, pk):
    if request.method == "POST":
        data = request.POST
        winner_id = data.get("winner")
        loser_id = data.get("loser")
        is_double_loss = "is_double_loss" in data

        winner = get_object_or_404(Player, pk=winner_id)
        loser = get_object_or_404(Player, pk=loser_id)
        standing = get_object_or_404(models.Standing, pk=pk)

        models.MatchResult.objects.create(
            standing=standing,
            winner=winner,
            loser=loser,
            is_double_loss=is_double_loss,
        )

        return redirect(reverse("match-results", args=[standing.pk]))
    return redirect("/")
