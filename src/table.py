from typing import Iterator
from bet import Bet
from roulette import InvalidBet


class Table:
    """
    :class:`Table` contains all the :class:`Bet` instances created by a :class:`Player` object. A
    table also has a betting limit, and the sum of all of a player’s bets must be less than or
    equal to this limit. We assume a single :class:`Player` object in the simulation.

    .. attribute:: limit

       This is the table limit. The sum of the bets from a :class:`Player` object must be less than
       or equal to this limit.

    .. attribute:: minimum

       This is the table minimum. Each individual bet from a :class:`Player` object must be greater
       than this limit.

    .. attribute:: bets

       This is a **list** of the :class:`Bet` instances currently active. These will result in
       either wins or losses to the :class:`Player` object.

    """

    def __init__(self, *bets) -> None:
        """
        Creates an empty **list** of bets.

        :param bets: A sequence of :class:`Bet` instances to initialize the table. If omitted,
                    an empty **list** will be used.
        """

        self.bets = list(bets) if bets else []
        self.minimum = 1
        self.limit = 300

    def placeBet(self, bet: Bet) -> None:
        """
        Adds the :class:`Bet` instance to the list of current bets.

        :param bet: A :class:`Bet` instance to be added to the table.
        """

        self.bets.append(bet)

    def __iter__(self) -> Iterator[Bet]:
        """
        Returns an iterator over the available list of :class:`Bet` instances. This simply returns
        the iterator over the list of :class:`Bet` objects.

        :return: iterator over all bets.
        """

        return iter(self.bets)

    def isValid(self) -> None:
        """
        **Raises:** :class:`InvalidBet` if the bets don’t pass the table limit rules.

        Applies the table-limit rules:

            - The sum of all bets is less than or equal to the table limit.

            - All bet amounts are greater than or equal to the table minimum.

        If there’s a problem an :class:`InvalidBet` exception is raised.
        """

        bets_sum = 0
        for bet in self.bets:
            bets_sum += bet.amount
            if bet.amount < self.minimum or bets_sum > self.limit:
                raise InvalidBet

    def __str__(self) -> str:
        """
        Returns an easy-to-read string representation of all current bets.

        :return: str
        """

        bet_strings = [str(bet) for bet in self.bets]
        if not bet_strings:
            return "No current bets"
        return "Current bets: \n:" + "\n".join(bet_strings)

    def __repr__(self) -> str:
        """
        Returns a representation of the form  :samp:`Table(bet, bet, ...)`.

        :return: str
        """

        bet_reprs = ", ".join(repr(bet) for bet in self.bets)
        return f"Table({bet_reprs})"
