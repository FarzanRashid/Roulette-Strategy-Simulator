from typing import Set
from outcome import Outcome
from .martingale import Martingale


class SevenReds(Martingale):
    def __init__(self, table):
        super().__init__(table)
        self.redCount = 7

    def placeBets(self) -> None:
        if self.redCount == 0:
            super().placeBets()

    def winners(self, outcomes: Set[Outcome]) -> None:
        red_outcome = Outcome("Red", 1)
        if red_outcome in outcomes:
            self.redCount -= 1
        else:
            self.redCount = 7
