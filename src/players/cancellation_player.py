from outcome import Outcome
from table import Table
from bet import Bet
from players.player import Player


class PlayerCancellation(Player):
    def __init__(self, table: Table) -> None:
        super().__init__(table)
        self.outcome = Outcome("Red", 1)
        self.sequence: list[int] = []
        self.bet_amount = 0
        self.resetSequence()

    def resetSequence(self) -> None:
        self.sequence = [1, 2, 3, 4, 5, 6]

    def placeBets(self) -> None:
        self.bet_amount = self.sequence[0] + self.sequence[-1]
        self.table.placeBet(Bet(self.bet_amount, self.outcome))
        self.stake -= self.bet_amount

    def win(self, bet: Bet) -> None:
        super().win(bet)
        self.sequence.pop()
        self.sequence.pop(0)

    def lose(self, bet: Bet) -> None:
        self.sequence.append(bet.amount)

    def playing(self) -> bool:
        if not super().playing() or len(self.sequence) < 2 or self.stake < self.bet_amount:
            self.resetSequence()
            return False
        return True
