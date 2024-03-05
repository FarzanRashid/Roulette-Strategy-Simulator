from outcome import Outcome
from table import Table
from bet import Bet
from players.player import Player


class PlayerCancellation(Player):
    """
    :class:`PlayerCancellation` uses the cancellation betting system. This player allocates their
    available budget into a sequence of bets that have an accelerating potential gain as well as
    recouping any losses.

    .. attribute:: sequence

       This **List** keeps the bet amounts; wins are removed from this list and losses are
       appended to this list. THe current bet is the first value plus the last value.

    .. attribute:: outcome

       This is the player’s preferred :py:class:`~outcome.Outcome` instance.
    """

    def __init__(self, table: Table) -> None:
        """
        This uses the **PlayerCancellation.resetSequence()** method to initialize the
        sequence of numbers used to establish the bet amount. This also picks a suitable even money
        :py:class:`~outcome.Outcome`, for example, black.

        :param table: The  object :py:class:`~table.Table` which will accept the bets.
        """

        super().__init__(table)
        self.outcome = Outcome("Red", 1)
        self.sequence: list[int] = []
        self.bet_amount = 0
        self.resetSequence()

    def resetSequence(self) -> None:
        """
        Puts the initial sequence of six values, ``[1, 2, 3, 4, 5, 6]`` into the **sequence**
        variable. The sequence ``[1, 1, 1, 1, 1, 1]`` will also work, and the bets will be smaller.
        """

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
        if (
            not super().playing()
            or len(self.sequence) < 2
            or self.stake < self.bet_amount
        ):
            self.resetSequence()
            return False
        return True
