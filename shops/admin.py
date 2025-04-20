from django.contrib import admin

from shops import models


# Register your models here.


@admin.register(models.Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ["name", "country", "is_active"]
    list_filter = ["is_active", "country"]
    search_fields = ["name", "address"]
    ordering = ["name"]
    list_editable = ["is_active"]
