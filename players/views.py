from django.shortcuts import render

from players import models
# Create your views here.


def all_stats(request):
    players_with_global_stats = (
        models.Player.objects.with_winrate().order_by().exclude(winrate=None)
    )
    context = {
        "players": players_with_global_stats,
    }

    return render(
        request=request,
        context=context,
        template_name="all_stats.html",
    )
