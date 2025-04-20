from typing import override
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


from tournaments import models as tournaments_models

from shops import models as shops_models
from players import models as players_models


class Command(BaseCommand):
    help = "Init data"

    @override
    def handle(self, *args, **options):
        password = "kamiHanaKana2025"
        if not User.objects.filter(username="kami").exists():
            self.stdout.write(f"Create kami user; with password: '{password}'")
            User.objects.create_superuser(username="kami", password=password)

        self.stdout.write("Create 'godtier' player")
        players_models.Player.objects.get_or_create(
            identifier="godtier",
        )
        self.stdout.write("Create 'test' shop")
        test_shop = shops_models.Shop.objects.get_or_create(
            name="test",
            address="yay bat yay",
            country="FR",
        )[0]
        self.stdout.write("Create '2025' season")
        five_season = tournaments_models.Season.objects.get_or_create(
            name="2025",
        )[0]

        self.stdout.write("Create 'hey hey' tournament")
        tournaments_models.Tournament.objects.get_or_create(
            number=1,
            shop=test_shop,
            description="hey hey",
            season=five_season,
        )
