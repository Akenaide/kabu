from dataclasses import dataclass


@dataclass
class ParticipationDataFromImport:
    rank: int
    identifier: str
    swiss_win: int
