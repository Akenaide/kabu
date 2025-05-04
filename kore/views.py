from django.template.response import SimpleTemplateResponse

from tournaments import models as tm
from players import models as pm
from shops import models as sm


def home(request):
    """Home page view providing an overview of the application."""
    context = {
        "tournaments_count": tm.Tournament.objects.count(),
        "players_count": pm.Player.objects.count(),
        "shops_count": sm.Shop.objects.all().count(),
        "seasons": tm.Season.objects.all(),
        "recent_tournaments": tm.Tournament.objects.order_by("-date")[:5],
    }
    return SimpleTemplateResponse(
        "home.html",
        context=context,
    )
