import random
from dataclasses import dataclass


@dataclass(frozen=True)
class Outcome:
    """
    :class:`Outcome` contains a single outcome on which a bet can be placed.

    In Roulette, each spin of the wheel has a number of :class:`Outcome` objects with bets that
    will be paid off. For example, the “1” bin has the following winning :class:`Outcome`
    instances: “1”, “Red”, “Odd”, “Low”, “Column 1”, “Dozen 1-12”, “Split 1-2”, “Split 1-4”,
    “Street 1-2-3”, “Corner 1-2-4-5”, “Five Bet”, “Line 1-2-3-4-5-6”, “00-0-1-2-3”, “Dozen 1”,
    “Low” and “Column 1”.

    All of thee above-named bets will pay off if the wheel spins a “1”. This makes a Wheel and a
    Bin fairly complex containers of :class:`Outcome` objects.

    ..  attribute:: name

        Holds the name of the Outcome. Examples include "1", "Red".

    .. attribute:: odds

        Holds the payout odds for this Outcome. Most odds are stated as 1:1 or 17:1, we only keep
        the numerator (17) and assume the denominator is 1.

    """

    name: str
    odds: int

    def __str__(self) -> str:
        """
        Easy-to-read representation of outcome instances.

        :return: String of the form *name (odds*:1).
        :rtype: str
        """
        return f"{self.name:s} ({self.odds:d}:1)"

    def winAmount(self, amount: float) -> float:
        """
        Multiply this :class:`Outcome`'s odds by the given amount. The product is returned.

        :param amount: amount being bet
        :type amount: float
        """
        return self.odds * amount


class Bin(frozenset):
    """
    :class:`Bin` contains a collection of :class:`Outcome` instances which reflect the winning bets
    that are paid for a particular bin on a Roulette wheel. In Roulette, each spin of the wheel
    has a number of :class:`Outcome` instances. Example: A spin of 1, selects the “1” bin with
    the following winning :class:`Outcome` instances: “1” , “Red”, “Odd”,“Low” , “Column 1” ,
    “Dozen 1-12” , “Split 1-2” , “Split 1-4” , “Street 1-2-3” , “Corner 1-2-4-5”, “Five Bet”,
    “Line 1-2-3-4-5-6” , “00-0-1-2-3” , “Dozen 1”, “Low” and “Column 1”. These are collected into a
    single :class:`Bin`.
    """


class Wheel:
    """
    :class:`Wheel` contains the 38 individual bins on a Roulette wheel, plus a random number
    generator. It can select a :class:`Bin` at random, simulating a spin of the Roulette wheel.

    .. attribute:: bins

        Contains the individual Bin instances.

        This is a tuple of 38 elements. This can be built with ``tuple(Bin() for i in
        range(38))``

    .. attribute:: rng

        A random number generator to select a :class:`Bin` from the **bins** collection.

        For testing, we’ll often want to seed this generator. For simulation processing, we can
        set the seed value using ``os.urandom()``.
    """

    def __init__(self) -> None:
        """
        Creates a new wheel with 38 empty Bin instances. It will also create a new random number
        generator instance.

        At the present time, this does not do the full initialization of the Bin instances. We’ll
        rework this in a future exercise.
        """
        self.bins = tuple(Bin() for _ in range(38))
        self.rng = random.Random()

    def addOutcome(self, number: int, outcome: Outcome) -> None:
        """
        Adds the given :class:`Outcome` object to the :class:`Bin` instance with the given number.

        :param number: bin number, in the range zero to 37 inclusive.
        :type number: int
        :param outcome: The Outcome to add to this Bin
        :type outcome: Outcome
        """
        updated_bin = Bin(list(self.bins[number].union(Bin([outcome]))))
        self.bins = self.bins[:number] + (updated_bin,) + self.bins[number + 1:]

    def choose(self) -> Bin:
        """
        Generates a random number between 0 and 37, and returns the randomly selected Bin instance.

        The **Random.choice()** function of the **random** module will select one of the available
        :class:`Bin` instances from the **bins** collection.

        :return: A Bin selected at random from the wheel.
        :rtype: Bin
        """
        return self.rng.choice(self.bins)

    def get(self, bin: int) -> Bin:
        """
        Returns the given Bin instance from the internal collection.

        :param bin: bin number, in the range zero to 37 inclusive.
        :type bin: int
        :return: The requested Bin.
        :rtype: Bin
        """
        return self.bins[bin]


class BinBuilder:
    def __init__(self) -> None:
        pass

    def buildBins(self, wheel: Wheel) -> None:
        self.create_straight_bets(wheel)

    @staticmethod
    def create_straight_bets(wheel: Wheel) -> None:
        odd_for_straight_bet = 35
        straight_bet_numbers = set(_ for _ in range(37))

        for i in straight_bet_numbers:
            straight_bet = Outcome(str(i), odd_for_straight_bet)
            wheel.addOutcome(i, straight_bet)
        zero_zero_bet = Outcome("00", 35)
        bin_index_of_zero_zero_outcome = 37
        wheel.addOutcome(bin_index_of_zero_zero_outcome, zero_zero_bet)
