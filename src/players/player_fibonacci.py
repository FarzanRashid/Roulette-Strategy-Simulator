from bet import Bet
from players.player import Player
from table import Table
from outcome import Outcome


class PlayerFibonacci(Player):
    """
    :class:`PlayerFibonacci` uses the Fibonacci betting system. This player allocates their
    available budget into a sequence of bets that have an accelerating potential gain.

    .. attribute:: recent

       This is the most recent bet amount. Initially, this is 1.

    .. attribute:: previous

       This is the bet amount previous to the most recent bet amount. Initially, this is zero.
    """

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
        if not super().playing() or self.stake < self.bet_amount:
            self.recent = 1
            self.previous = 0
            self.bet_amount = self.recent + self.previous
            return False
        return True

    def placeBets(self) -> None:
        self.table.placeBet(Bet(self.bet_amount, self.outcome))
        self.stake -= self.bet_amount
