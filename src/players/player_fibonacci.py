from bet import Bet
from players.player import Player
from table import Table
from outcome import Outcome


class PlayerFibonacci(Player):
    def __init__(self, table: Table) -> None:
        super().__init__(table)
        self.outcome = Outcome("Black", 1)
        self.recent = 1
        self.previous = 0
        self.bet_amount = self.recent + self.previous

    def win(self, bet: Bet) -> None:
        super().win(bet)
        self.recent = 1
        self.previous = 0

    def lose(self, bet: Bet) -> None:
        self.bet_amount = self.recent + self.previous
        self.previous = self.recent
        self.recent = self.bet_amount

    def playing(self) -> bool:
        return super().playing() and self.roundsToGo > 0 and self.stake >= self.bet_amount

    def placeBets(self) -> None:
        self.table.placeBet(Bet(self.bet_amount, self.outcome))
