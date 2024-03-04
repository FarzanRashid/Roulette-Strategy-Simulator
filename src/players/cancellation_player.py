from outcome import Outcome
from table import Table
from bet import Bet
from players.player import Player


class PlayerCancellation(Player):
    def __init__(self, table: Table) -> None:
        super().__init__(table)
        self.outcome = Outcome("Red", 1)
        self.sequence = None
        self.resetSequence()

    def resetSequence(self) -> None:
        self.sequence = [1, 2, 3, 4, 5, 6]

    def placeBets(self) -> None:
        bet_amount = self.sequence[0] + self.sequence[-1]
        self.table.placeBet(Bet(bet_amount, self.outcome))
        self.stake -= bet_amount

    def win(self, bet: Bet) -> None:
        super().win(bet)
        self.sequence.pop()
        self.sequence.pop(0)
