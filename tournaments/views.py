from django.template.response import SimpleTemplateResponse

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
