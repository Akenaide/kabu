from django.contrib import admin
from players import models
# Register your models here.


@admin.register(models.Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ["pk", "identifier", "verbose_name"]
    search_fields = ["identifier", "verbose_name"]
    ordering = ["identifier"]
