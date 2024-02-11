import random
from typing import Dict, Iterator
from dataclasses import dataclass
from abc import ABC, abstractmethod


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


class Passenger57(Player):
    """
    :class:`Passenger57` constructs a :class:`Bet` instance based on the :class:`Outcome` object
    named :samp:`"Black"`. This is a very persistent player.

    .. attribute:: black

       This is the outcome on which this player focuses their betting.

       This :class:`Player` will get this from the :class:`Wheel` using a well-known bet name.

    .. attribute:: table

       The :class:`Table` that is used to place individual :class:`Bet` instances.

    """

    def __init__(self, table: Table, wheel: Wheel) -> None:
        """
        Constructs the :class:`Player` instance with a specific table for placing bets. This also
        creates the “black” :class:`Outcome`. This is saved in a variable named
        **Passenger57.black** for use in creating bets.

        :param table: The :class:`Table` instance on which bets are placed.
        :param wheel: The :class:`Wheel` instance which defines all :class:`Outcome` instances.
        """

        super().__init__(table)
        self.table = table
        self.wheel = wheel
        self.black = self.wheel.getOutcome("Black")

    def placeBets(self) -> None:
        """
        Updates the :class:`Table` object with the various bets. This version creates a :class:`Bet`
        instance from the “Black” :class:`Outcome` instance. It uses **Table.placeBet()** to
        place that bet.

        """

        bet_amount = 20
        bet = Bet(bet_amount, self.black)
        self.table.placeBet(bet)
        self.stake -= bet_amount


def main() -> None:  # pragma: no cover
    """
    A main application function that creates the necessary objects, runs the Simulator’s gather()
    method, and writes the available outputs to sys.stdout
    """
    wheel = Wheel()
    bin_builder = BinBuilder()
    table = Table()
    game = Game(wheel, table)
    martingale = Martingale(table)
    simulator = Simulator(game, martingale)

    bin_builder.buildBins(wheel)
    simulator.gather()

    print("maxima: ", simulator.maxima)
    print("duration: ", simulator.durations)


if __name__ == "__main__":
    main()  # pragma: no cover
