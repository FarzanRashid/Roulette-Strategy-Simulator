from abc import ABC, abstractmethod
from table import Table
from bet import Bet


class Player(ABC):
    """
    :class:`Player` places bets in Roulette. This an abstract class, with no actual body for the
    **Player.placeBets()** method. However, this class does implement the basic **Player.win(
    )** method used by all subclasses.

    .. attribute::  stake

       The player’s current stake. Initialized to the player’s starting budget.

    .. attribute:: roundsToGo

       The number of rounds left to play. Initialized by the overall simulation control to the
       maximum number of rounds to play. In Roulette, this is spins. In Craps, this is the number of
       throws of the dice, which may be a large number of quick games or a small number of
       long-running games. In Craps, this is the number of cards played, which may be large
       number of hands or small number of multi-card hands.

    .. attribute:: table

       The :class:`Table` object used to place individual :class:`Bet` instances. The :class:`Table`
       object contains the current :class:`Wheel` object from which the player can get
       :class:`Outcome` objects used to build :class:`Bet` instances.
    """

    def __init__(self, table: Table) -> None:
        """
        Constructs the :class:`Player` instance with a specific :class:`Table` object for placing
        :class:`Bet` instances.

        :param table:  the table to use

        Since the table has access to the Wheel instance, we can use this wheel to extract
        :class:`Outcome` objects.
        """

        self.table = table
        self.stake = 100
        self.roundsToGo = 250

    def win(self, bet: Bet) -> None:
        """
        :param bet: The bet which won

        Notification from the :class:`Game` object that the :class:`Bet` instance was a winner. The
        amount of money won is available via the **Bet.winAmount()** method.
        """

        self.stake += bet.winAmount()

    def lose(self, bet: Bet) -> None:
        """
        :param bet: The bet which won

        Notification from the :class:`Game` object that the :class:`Bet` instance was a loser. Note
        that the amount was already deducted from the stake when the bet was created.
        """

    @abstractmethod
    def placeBets(self) -> None:
        """
        Updates the :class:`Table` object with the various :class:`Bet` objects.

        When designing the :class:`Table` class, we decided that we needed to deduct the amount of a
        bet from the stake when the bet is created. See the Table **Roulette Table Analysis**
        for more information.
        """

    def playing(self) -> bool:
        """
        Returns :samp:`True` while the player is still active.
        """
        return self.stake >= self.table.minimum and self.roundsToGo > 0
