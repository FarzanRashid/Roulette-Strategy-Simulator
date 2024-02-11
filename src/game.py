from wheel import Wheel
from table import Table
from players.player import Player


class Game:
    """
    :class:`Game` manages the sequence of actions that defines the game of Roulette. This includes
    notifying the :class:`Player` object to place bets, spinning the :class:`Wheel` object and
    resolving the :class:`Bet` instances actually present on the :class:`Table` object.

    .. attribute:: wheel

       The :class:`Wheel` instance that returns a randomly selected :class:`Bin` object of
       :class:`Outcome` instances.

    .. attribute:: table

       The :class:`Table` object which contains the :class:`Bet` instances placed by the
       :class:`Player` object.

    .. attribute:: player

       The :class:`Player` object which creates :class:`Bet` instances at the :class:`Table` object.

    """

    def __init__(self, wheel: Wheel, table: Table) -> None:
        """
        Constructs a new :class:`Game`, using a given :class:`Wheel` and :class:`Table`.

        :param wheel: The :class:`Wheel` instance which produces random events
        :param table: The :class:`Table` instance which holds bets to be resolved.
        """

        self.wheel = wheel
        self.table = table

    def cycle(self, player: Player) -> None:
        """
        :param player: the individual player that places bets, receives winnings and pays losses.

        This will execute a single cycle of play with a given :class:`Player`. It will execute the
        following steps:

        1. Call **Player.placeBets()** method to create bets.
        2. Call **Wheel.choose()** method to get the next winning :class:`Bin` object.
        3. Call **iter()** on the :class:`table` to get all of the :class:`Bet` instances.
           For each :class:`Bet` instance, if the winning :class:`Bin` contains the
           :class:`Outcome`, call **Player.win()** method, otherwise, call the
           **Player.lose()** method.
        """

        player.placeBets()
        winning_bin = self.wheel.choose()
        for bet in self.table:
            if bet.outcome in winning_bin:
                player.win(bet)
            else:
                player.lose(bet)
