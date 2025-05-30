from __future__ import annotations
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from players.models import Player


@dataclass
class PlayerStatsVsPlayer:
    val: float | None | str
    player: Player | None = None

    @property
    def css_classes(self):
        if self.val is None:
            return "has-text-grey-lighter"
        elif isinstance(self.val, str):
            ""
        elif self.val > 50.0:
            return "has-background-success-light"
        elif self.val < 50.0:
            return "has-background-danger-light"
        else:
            return ""
