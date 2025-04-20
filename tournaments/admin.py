from django.contrib import admin
from tournaments import models
# Register your models here.


@admin.register(models.Season)
class SeasonAdmin(admin.ModelAdmin):
    list_display = ["pk", "name"]


@admin.register(models.Tournament)
class TournamentAdmin(admin.ModelAdmin):
    list_display = ["pk", "number", "date", "season", "shop"]
    list_filter = ["season", "shop"]
    search_fields = ["description"]


@admin.register(models.Participation)
class ParticipationAdmin(admin.ModelAdmin):
    list_display = ["pk", "player", "swiss_win", "final_standing", "standing"]
    list_filter = ["standing"]
    search_fields = ["player__name"]  # Assuming player has a name field


@admin.register(models.Standing)
class StandingAdmin(admin.ModelAdmin):
    list_display = ["pk", "tournament"]
    search_fields = ["tournament__description"]
