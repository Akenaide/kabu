from dataclasses import dataclass


@dataclass
class PlayerStatsVsPlayer:
    val: float | None | str

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
