# Generated by Django 5.2 on 2025-05-04 21:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("players", "0001_initial"),
        ("tournaments", "0002_alter_participation_options_alter_tournament_date"),
    ]

    operations = [
        migrations.CreateModel(
            name="MatchResult",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("is_double_loss", models.BooleanField(default=False)),
                (
                    "looser",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="matchs_lost",
                        to="players.player",
                    ),
                ),
                (
                    "standing",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="tournaments.standing",
                    ),
                ),
                (
                    "winner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="matchs_won",
                        to="players.player",
                    ),
                ),
            ],
        ),
    ]
