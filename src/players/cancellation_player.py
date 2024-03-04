from outcome import Outcome
from table import Table
from players.player import Player


class PlayerCancellation(Player):
    def __init__(self, table: Table) -> None:
        super().__init__(table)
        self.outcome = Outcome("Red", 1)
        self.sequence = None
        self.resetSequence()