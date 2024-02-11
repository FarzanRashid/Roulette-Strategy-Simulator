from table import Table
from outcome import Outcome
from bet import Bet
from invalid_bet import InvalidBet
from .player import Player


class Martingale(Player):
    """
    :class:`Martingale` is a :class:`Player` who places bets in Roulette. This player doubles their
    bet on every loss and resets their bet to a base amount on each win.

    .. attribute:: losscount

       The number of losses. This is the number of times to double the bet.

    .. attribute:: betMultiple

       The the bet multiplier, based on the number of losses. This starts at 1, and is reset to 1 on
       each win. It is doubled in each loss. This is always equal to :math:`2^{lossCount}`.
    """

    def __init__(self, table: Table):
        """
        Constructs the :class:`Martingale` :class:`Player` instance with a specific :class:`Table`
        object for placing :class:`Bet` instances.

        :param table: the table to use
        """

        super().__init__(table)
        self.losscount = 0
        self.betMultiple = 1

    def placeBets(self) -> None:
        """
        Updates the :class:`Table` object with a bet on “black”. The amount bet is
        :math:`2^{lossCount}`, which is the value of **betMultiple**.
        """

        outcome = Outcome("Black", 1)
        bet = Bet(self.betMultiple, outcome)
        self.table.placeBet(bet)
        try:
            self.table.isValid()
        except InvalidBet as exc:
            self.losscount = 0
            self.betMultiple = 2**self.losscount
            raise InvalidBet from exc
        self.stake -= self.betMultiple

    def playing(self) -> bool:
        if not super().playing() or self.betMultiple > self.stake:
            self.losscount = 0
            self.betMultiple = 2**self.losscount
            return False
        return True

    def win(self, bet: Bet) -> None:
        """
        :param bet: The bet which won

        Notification from the :class:`Game` object that the :class:`Bet` instance was a winner. The
        amount of money won is available via the **Bet.winAmount()** method.
        """

        super().win(bet)
        self.losscount = 0
        self.betMultiple = 2**self.losscount

    def lose(self, bet: Bet):
        """
        :param bet:

        Uses the superclass **Player.loss()** to do whatever bookkeeping the superclass already
        does.
        Increments **lossCount** by :samp:`1` and doubles **betMultiple**.
        """

        super().lose(bet)
        self.losscount += 1
        self.betMultiple = 2**self.losscount
