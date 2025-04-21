import csv
from io import StringIO
from django.contrib import admin
from django.db import transaction
from django.http import HttpResponseRedirect
from tournaments import models
from tournaments.dataclasses import ParticipationDataFromImport
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
    ordering = ["pk"]


@admin.register(models.Standing)
class StandingAdmin(admin.ModelAdmin):
    change_form_template = "admin_standing_import_change_form.html"
    list_display = ["pk", "tournament"]
    search_fields = ["tournament__description"]

    def import_csv(self, csv_list, standing):
        with transaction.atomic():
            for line in csv_list:
                models.Participation.objects.create_from_import(
                    data=ParticipationDataFromImport(
                        rank=int(line["rank"]),
                        identifier=line["name"],
                        swiss_win=int(
                            line["swiss_win"],
                        ),
                    ),
                    standing=standing,
                )

    def response_change(self, request, obj):
        if "_import-standing" in request.POST:
            csv_file = StringIO(request.POST["new-standing"])
            reader = csv.DictReader(csv_file)
            csv_list = list(reader)
            self.import_csv(csv_list=csv_list, standing=obj)
            self.message_user(request, "Standing imported")
            return HttpResponseRedirect(".")
        return super().response_change(request, obj)
