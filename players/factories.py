import uuid
from players import models


def make_player() -> models.Player:
    return models.Player.objects.create(
        identifier=str(uuid.uuid4()),
        verbose_name=str(uuid.uuid4()),
    )
