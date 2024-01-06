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
    """
    :class:`BinBuilder` creates the :class:`Outcome` instances for all of the 38 individual
    :class:`Bin` on a Roulette wheel.
    """
    def __init__(self) -> None:
        pass

    def buildBins(self, wheel: Wheel) -> None:
        self.build_bins_for_straight_bets(wheel)
        self.build_bins_for_horizontal_split_bets(wheel)
        self.build_bins_for_vertical_split_bets(wheel)
        self.build_bins_for_street_bets(wheel)
        self.build_bins_for_corner_bets(wheel)
        self.build_bins_for_line_bets(wheel)
        self.build_bins_for_five_bet(wheel)
        self.build_bins_for_even_money_bets(wheel)
        self.build_bins_for_dozen_bets(wheel)
        self.build_bins_for_column_bets(wheel)

    @staticmethod
    def build_bins_for_straight_bets(wheel: Wheel) -> None:
        straight_bet_odds = 35
        straight_bet_numbers = set(range(37))

        for number in straight_bet_numbers:
            straight_bet_outcome = Outcome(str(number), straight_bet_odds)
            wheel.addOutcome(number, straight_bet_outcome)
        zero_zero_bet_outcome = Outcome("00", straight_bet_odds)
        bin_index_of_zero_zero_outcome = 37
        wheel.addOutcome(bin_index_of_zero_zero_outcome, zero_zero_bet_outcome)

    @staticmethod
    def build_bins_for_horizontal_split_bets(wheel: Wheel) -> None:
        split_bet_odds = 17

        split_bet_numbers = {number * 3 + 1 for number in range(12)} | {number * 3 + 2 for number
                                                                        in range(12)}
        for number in split_bet_numbers:
            horizontal_split_bet_outcome = Outcome(str(number) + "-" + str(number + 1),
                                                   split_bet_odds)
            wheel.addOutcome(number, horizontal_split_bet_outcome)
            wheel.addOutcome(number + 1, horizontal_split_bet_outcome)

    @staticmethod
    def build_bins_for_vertical_split_bets(wheel: Wheel) -> None:
        split_bet_odds = 17
        vertical_split_bet_numbers = set(range(1, 34))
        for number in vertical_split_bet_numbers:
            vertical_split_bet_outcome = Outcome(str(number) + "-" + str(number + 3),
                                                 split_bet_odds)
            wheel.addOutcome(number, vertical_split_bet_outcome)
            wheel.addOutcome(number + 3, vertical_split_bet_outcome)

    @staticmethod
    def build_bins_for_street_bets(wheel: Wheel) -> None:
        street_bet_odds = 11
        street_bet_numbers = set(number * 3 + 1 for number in range(12))
        for number in street_bet_numbers:
            street_bet_outcome = Outcome(
                str(number) + "-" + str(number + 1) + "-" + str(number + 2),
                street_bet_odds)
            wheel.addOutcome(number, street_bet_outcome)
            wheel.addOutcome(number + 1, street_bet_outcome)
            wheel.addOutcome(number + 2, street_bet_outcome)

    @staticmethod
    def build_bins_for_corner_bets(wheel: Wheel) -> None:
        odds_for_corner_bet = 8

        corner_bet_numbers = {number * 3 + 1 for number in range(11)} | {number * 3 + 2 for
                                                                         number in range(11)}
        for number in corner_bet_numbers:
            corner_bet_outcome = Outcome(str(number) + "-" + str(number + 1) + "-" +
                                         str(number + 3) + "-" + str(number + 4),
                                         odds_for_corner_bet)

            wheel.addOutcome(number, corner_bet_outcome)
            wheel.addOutcome(number + 1, corner_bet_outcome)
            wheel.addOutcome(number + 3, corner_bet_outcome)
            wheel.addOutcome(number + 4, corner_bet_outcome)

    @staticmethod
    def build_bins_for_line_bets(wheel: Wheel) -> None:
        line_bet_odds = 5
        line_bet_numbers = {number * 3 + 1 for number in range(11)}
        for number in line_bet_numbers:
            line_bet_outcome = Outcome(str(number) + "-" + str(number + 1) + "-" + str(number + 2)
                                       + "-" + str(number + 3) + "-" + str(number + 4) + "-" +
                                       str(number + 5), line_bet_odds)
            wheel.addOutcome(number, line_bet_outcome)
            wheel.addOutcome(number + 1, line_bet_outcome)
            wheel.addOutcome(number + 2, line_bet_outcome)
            wheel.addOutcome(number + 3, line_bet_outcome)
            wheel.addOutcome(number + 4, line_bet_outcome)
            wheel.addOutcome(number + 5, line_bet_outcome)

    @staticmethod
    def build_bins_for_five_bet(wheel: Wheel) -> None:
        odds_for_five_bet = 6
        five_bet_name = "00-0-1-2-3"
        five_bet_outcome = Outcome(five_bet_name, odds_for_five_bet)
        bin_indexes_for_five_bet = {0, 1, 2, 3, 37}

        for index in bin_indexes_for_five_bet:
            wheel.addOutcome(index, five_bet_outcome)

    @staticmethod
    def build_bins_for_even_money_bets(wheel: Wheel) -> None:
        even_bet_odds = 1

        red_bet_name = "Red"
        black_bet_name = "Black"
        low_bet_name = "Low"
        high_bet_name = "High"
        even_bet_name = "Even"
        odd_bet_name = "Odd"

        even_bet_numbers = set(range(1, 37))
        red_bet_numbers = {1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36}

        red_bet = Outcome(red_bet_name, even_bet_odds)
        black_bet = Outcome(black_bet_name, even_bet_odds)
        low_bet = Outcome(low_bet_name, even_bet_odds)
        high_bet = Outcome(high_bet_name, even_bet_odds)
        even_bet = Outcome(even_bet_name, even_bet_odds)
        odd_bet = Outcome(odd_bet_name, even_bet_odds)

        for number in even_bet_numbers:
            if number < 19:
                wheel.addOutcome(number, low_bet)
            if number >= 19:
                wheel.addOutcome(number, high_bet)
            if number % 2 == 0:
                wheel.addOutcome(number, even_bet)
            if number % 2 != 0:
                wheel.addOutcome(number, odd_bet)
            if number in red_bet_numbers:
                wheel.addOutcome(number, red_bet)
            if number not in red_bet_numbers:
                wheel.addOutcome(number, black_bet)

    @staticmethod
    def build_bins_for_dozen_bets(wheel: Wheel) -> None:
        dozen_bet_odds = 2
        for dozen in range(3):
            if dozen + 1 == 1:
                dozen_bet_name = "-".join([str(_) for _ in range(1, 13)])
                dozen_bet_outcome = Outcome(dozen_bet_name, dozen_bet_odds)
            elif dozen + 1 == 2:
                dozen_bet_name = "-".join([str(_) for _ in range(13, 25)])
                dozen_bet_outcome = Outcome(dozen_bet_name, dozen_bet_odds)
            else:
                dozen_bet_name = "-".join([str(_) for _ in range(25, 37)])
                dozen_bet_outcome = Outcome(dozen_bet_name, dozen_bet_odds)

            for bin_number in range(12):
                wheel.addOutcome(12 * dozen + bin_number + 1, dozen_bet_outcome)

    @staticmethod
    def build_bins_for_column_bets(wheel: Wheel) -> None:
        column_bet_odds = 2
        for column in range(3):
            if column + 1 == 1:
                column_bet_name = "-".join([str(_) for _ in range(1, 35, 3)])
                column_bet_outcome = Outcome(column_bet_name, column_bet_odds)
            elif column + 1 == 2:
                column_bet_name = "-".join([str(_) for _ in range(2, 36, 3)])
                column_bet_outcome = Outcome(column_bet_name, column_bet_odds)
            else:
                column_bet_name = "-".join([str(_) for _ in range(3, 37, 3)])
                column_bet_outcome = Outcome(column_bet_name, column_bet_odds)

            for bin_number in range(12):
                wheel.addOutcome(3 * bin_number + column + 1, column_bet_outcome)
