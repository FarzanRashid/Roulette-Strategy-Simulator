from players.player import Player
from table import Table
from outcome import Outcome


class PlayerFibonacci(Player):
    def __init__(self, table: Table) -> None:
        super().__init__(table)
        self.outcome = Outcome("Black", 1)
        self.recent = 1
        self.previous = 0
