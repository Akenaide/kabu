from django.template.response import SimpleTemplateResponse
from django.shortcuts import get_object_or_404

from tournaments import models
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
