import random
from typing import Dict, Iterator
from dataclasses import dataclass
from abc import ABC, abstractmethod


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
        self.all_outcomes: Dict[str, Outcome] = {}

    def addOutcome(self, number: int, outcome: Outcome) -> None:
        """
        Adds the given :class:`Outcome` object to the :class:`Bin` instance with the given number.

        :param number: bin number, in the range zero to 37 inclusive.
        :type number: int
        :param outcome: The Outcome to add to this Bin
        :type outcome: Outcome
        """
        updated_bin = Bin(list(self.bins[number].union(Bin([outcome]))))
        self.bins = self.bins[:number] + (updated_bin,) + self.bins[number + 1 :]

        self.all_outcomes[outcome.name] = outcome

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

    def getOutcome(self, name: str) -> Outcome:
        """
        Retrieve an :class:`Outcome` object based on the provided name.

        This method searches for an :class:`Outcome` with the specified name in the collection of
        all outcomes (`all_outcomes`). If the outcome is found, it is returned. Otherwise,
        a KeyError is raised with an error message.

        :param name: the name of an :class:`Outcome`
        :return: the :class:`Outcome` object
        :rtype: :class:`Outcome`
        """
        if name not in self.all_outcomes:
            raise KeyError(f"Outcome with {name} not found")
        return self.all_outcomes[name]


class BinBuilder:
    """
    :class:`BinBuilder` creates the :class:`Outcome` instances for all of the 38 individual
    :class:`Bin` on a Roulette wheel.
    """

    def __init__(self) -> None:
        """
        Initializes the :class:`BinBuilder`.
        """

    def buildBins(self, wheel: Wheel) -> None:
        """
        Creates the :class:`Outcome` instances and uses the **addOutcome()** method to place each
        :class:`Outcome` in the appropriate Bin of wheel.

        It’s then the :class:`Bin` instances responsibility to update the data structure used to
        store the :class:`Outcome` instances.

        :param wheel: The Wheel with Bins that must be populated with :class:`Outcome` instances.
        :type wheel: :class:`Wheel`
        """
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
        """
        Populates **Bin** for the given  **wheel** with straight bet outcomes, each associated
        with a unique number on the wheel.

        The function iterates through numbers 0 to 36 and creates a straight bet outcome for each
        number, each with an associated odds value of 35. Additionally, a straight bet outcome
        for the "00" is created with the same odds.

        :param wheel: The Wheel object to which the straight bet outcomes will be added.
        :type wheel: :class:`Wheel`

        **Note**: The wheel is assumed to have bins for numbers 0 to 36, and an extra bin at
        index 37 for the "00" outcome.
        """
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
        """
        Populates **Bin** for the given  **wheel** with straight bet outcomes, each associated
        with a unique number on the wheel.


        This method adds horizontal split bet outcomes for pairs of horizontally adjacent numbers on
        the wheel. For each pair, a horizontal split bet outcome is created with an associated odds
        value of 17. Each outcome corresponds to a bet on the line between two horizontally
        adjacent numbers.

        The function considers pairs of numbers formed by adding 1 and 2 successively to each
        multiple of 3 within the range of 0 to 33 (inclusive).


        :param wheel: The Wheel object to which the horizontal split bet outcomes will be added.
        :type wheel: :class:`Wheel`

        **Note**: The wheel is assumed to have bins for all possible numbers, and the split bet
        outcomes are added for pairs of horizontally adjacent numbers.
        """
        split_bet_odds = 17

        split_bet_numbers = {_ * 3 + 1 for _ in range(12)} | {
            _ * 3 + 2 for _ in range(12)
        }
        for number in split_bet_numbers:
            horizontal_split_bet_outcome = Outcome(
                str(number) + "-" + str(number + 1), split_bet_odds
            )
            wheel.addOutcome(number, horizontal_split_bet_outcome)
            wheel.addOutcome(number + 1, horizontal_split_bet_outcome)

    @staticmethod
    def build_bins_for_vertical_split_bets(wheel: Wheel) -> None:
        """
        Populates **Bin** for the given **wheel** with vertical split bet outcomes, each associated
        with a pair of vertically adjacent numbers on the wheel.

        The function iterates through pairs of vertically adjacent numbers on the wheel and creates
        a vertical split bet outcome for each pair, each with an associated odds value of 17. Each
        outcome corresponds to a bet on the line between two vertically adjacent numbers.


        :param wheel: The Wheel object to which the vertical split bet outcomes will be added.
        :type wheel: Wheel


        **Note**: The wheel is assumed to have bins for all possible numbers, and the split bet
        outcomes are added for pairs of vertically adjacent numbers.
        """
        split_bet_odds = 17
        vertical_split_bet_numbers = set(range(1, 34))
        for number in vertical_split_bet_numbers:
            vertical_split_bet_outcome = Outcome(
                str(number) + "-" + str(number + 3), split_bet_odds
            )
            wheel.addOutcome(number, vertical_split_bet_outcome)
            wheel.addOutcome(number + 3, vertical_split_bet_outcome)

    @staticmethod
    def build_bins_for_street_bets(wheel: Wheel) -> None:
        """
        Populates **Bin** for the given **wheel** with street bet outcomes, each associated with a
        set of three consecutive numbers on the wheel.

        The function iterates through sets of three consecutive numbers on the wheel and creates a
        street bet outcome for each set, each with an associated odds value of 11. Each outcome
        corresponds to a bet on the line covering three consecutive numbers.

        :param wheel: The Wheel object to which the street bet outcomes will be added.
        :type wheel: :class:`Wheel`

        **Note**: The **wheel** is assumed to have bins for all possible numbers, and the street
        bet outcomes are added for sets of three consecutive numbers.
        """
        street_bet_odds = 11
        street_bet_numbers = set(number * 3 + 1 for number in range(12))
        for number in street_bet_numbers:
            street_bet_outcome = Outcome(
                str(number) + "-" + str(number + 1) + "-" + str(number + 2),
                street_bet_odds,
            )
            wheel.addOutcome(number, street_bet_outcome)
            wheel.addOutcome(number + 1, street_bet_outcome)
            wheel.addOutcome(number + 2, street_bet_outcome)

    @staticmethod
    def build_bins_for_corner_bets(wheel: Wheel) -> None:
        """
        Populates **Bin** for the given **wheel** with corner bet outcomes, each associated with a
        set of four numbers forming a square on the wheel.

        The function iterates through sets of four numbers forming a square on the wheel and creates
        a corner bet outcome for each set, each with an associated odds value of 8. Each outcome
        corresponds to a bet on the intersection of lines covering four adjacent numbers.

        :param wheel: The Wheel object to which the corner bet outcomes will be added.
        :type wheel: :class:`Wheel`

        **Note**: The wheel is assumed to have bins for all possible numbers, and the corner bet
        outcomes are added for sets of four numbers forming a square.
        """
        odds_for_corner_bet = 8

        corner_bet_numbers = {number * 3 + 1 for number in range(11)} | {
            number * 3 + 2 for number in range(11)
        }
        for number in corner_bet_numbers:
            corner_bet_outcome = Outcome(
                str(number)
                + "-"
                + str(number + 1)
                + "-"
                + str(number + 3)
                + "-"
                + str(number + 4),
                odds_for_corner_bet,
            )

            wheel.addOutcome(number, corner_bet_outcome)
            wheel.addOutcome(number + 1, corner_bet_outcome)
            wheel.addOutcome(number + 3, corner_bet_outcome)
            wheel.addOutcome(number + 4, corner_bet_outcome)

    @staticmethod
    def build_bins_for_line_bets(wheel: Wheel) -> None:
        """
        Populates **Bin** for the given **wheel** with line bet outcomes, each associated
        with a set of six consecutive numbers on the wheel.

        The function iterates through sets of six consecutive numbers on the wheel and creates a
        line bet outcome for each set, each with an associated odds value of 5. Each outcome
        corresponds to a bet on the line covering six consecutive numbers.

        :param wheel: The Wheel object to which the line bet outcomes will be added.
        :type wheel: :class:`Wheel`

        **Note**: The wheel is assumed to have bins for all possible numbers, and the line bet
        outcomes are added for sets of six consecutive numbers.
        """
        line_bet_odds = 5
        line_bet_numbers = {number * 3 + 1 for number in range(11)}
        for number in line_bet_numbers:
            line_bet_outcome = Outcome(
                str(number)
                + "-"
                + str(number + 1)
                + "-"
                + str(number + 2)
                + "-"
                + str(number + 3)
                + "-"
                + str(number + 4)
                + "-"
                + str(number + 5),
                line_bet_odds,
            )
            wheel.addOutcome(number, line_bet_outcome)
            wheel.addOutcome(number + 1, line_bet_outcome)
            wheel.addOutcome(number + 2, line_bet_outcome)
            wheel.addOutcome(number + 3, line_bet_outcome)
            wheel.addOutcome(number + 4, line_bet_outcome)
            wheel.addOutcome(number + 5, line_bet_outcome)

    @staticmethod
    def build_bins_for_five_bet(wheel: Wheel) -> None:
        """
        Populates **Bin** for the given **wheel** with five bet outcomes, each associated with the
        "00-0-1-2-3" combination on the wheel.


        The function adds a single five bet outcome for the "00-0-1-2-3" combination, each with an
        associated odds value of 6. The outcome covers the numbers 0, 00, 1, 2, and 3.

        :param wheel: The Wheel object to which the five bet outcomes will be added.
        :type wheel: :class:`Wheel`


        **Note**: The wheel is assumed to have bins for the numbers 0, 00, 1, 2, 3, and an extra
        bin at index 37 for the "00" outcome.
        """
        odds_for_five_bet = 6
        five_bet_name = "00-0-1-2-3"
        five_bet_outcome = Outcome(five_bet_name, odds_for_five_bet)
        bin_indexes_for_five_bet = {0, 1, 2, 3, 37}

        for index in bin_indexes_for_five_bet:
            wheel.addOutcome(index, five_bet_outcome)

    @staticmethod
    def build_bins_for_even_money_bets(wheel: Wheel) -> None:
        """
        Populates **Bin** the given **wheel** with even money bet outcomes, each associated with
        even money bets in roulette.

        The function adds even money bet outcomes for Red, Black, Low, High, Even, and Odd bets,
        each with an associated odds value of 1.
        - Red and Black outcomes correspond to bets on the color of the number.
        - Low and High outcomes correspond to bets on numbers 1-18 and 19-36, respectively.
        - Even and Odd outcomes correspond to bets on even and odd numbers, respectively.

        :param wheel: The Wheel object to which the even money bet outcomes will be added.
        :type wheel: :class:`Wheel`

        **Note**: The wheel is assumed to have bins for all possible numbers.
        """
        even_bet_odds = 1

        red_bet_name = "Red"
        black_bet_name = "Black"
        low_bet_name = "Low"
        high_bet_name = "High"
        even_bet_name = "Even"
        odd_bet_name = "Odd"

        even_bet_numbers = set(range(1, 37))
        red_bet_numbers = {
            1,
            3,
            5,
            7,
            9,
            12,
            14,
            16,
            18,
            19,
            21,
            23,
            25,
            27,
            30,
            32,
            34,
            36,
        }

        for number in even_bet_numbers:
            if number < 19:
                wheel.addOutcome(number, Outcome(low_bet_name, even_bet_odds))
            else:
                wheel.addOutcome(number, Outcome(high_bet_name, even_bet_odds))
            if number % 2 == 0:
                wheel.addOutcome(number, Outcome(even_bet_name, even_bet_odds))
            else:
                wheel.addOutcome(number, Outcome(odd_bet_name, even_bet_odds))
            if number in red_bet_numbers:
                wheel.addOutcome(number, Outcome(red_bet_name, even_bet_odds))
            else:
                wheel.addOutcome(number, Outcome(black_bet_name, even_bet_odds))

    @staticmethod
    def build_bins_for_dozen_bets(wheel: Wheel) -> None:
        """
        Populates **Bin** the given **wheel** with dozen bet outcomes, each associated with one of
        the three dozens on the wheel.

        The function adds dozen bet outcomes for each of the three dozens (1-12, 13-24, 25-36),
        each with an associated odds value of 2. Each outcome corresponds to a bet on a set of
        twelve consecutive numbers in a dozen.

        :param wheel: The Wheel object to which the dozen bet outcomes will be added.
        :type wheel: :class:`Wheel`

        **Note**: The wheel is assumed to have bins for all possible numbers.
        """
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
        """
        Populates **Bin** for the given **wheel** with column bet outcomes, each associated with
        one of the three columns on the wheel.

        The function adds column bet outcomes for each of the three columns, each with an associated
        odds value of 2. Each outcome corresponds to a bet on a set of twelve consecutive numbers in
        a column.

        :param wheel: The Wheel object to which the column bet outcomes will be added.
        :type wheel: :class:`Wheel`

        Note: The wheel is assumed to have bins for all possible numbers.
        """
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


@dataclass
class Bet:
    """
    :class:`Bet` associates an amount and an :class:`Outcome`. In a future round of design, we can
    also associate a :class:`Bet` with a :class:`Player`.

    .. attribute:: amount

        The amount of the bet.

    .. attribute:: outcome

        The :class:`Outcome` on which the bet is placed.
    """

    amount: int
    outcome: Outcome

    def winAmount(self) -> int:
        """
        Uses the :class:`Outcome`’s **winAmount** to compute the amount won, given the amount of
        this bet. Note that the amount bet must also be added in. A 1:1 outcome (e.g. a bet on Red)
        pays the amount bet plus the amount won.

        :return:  amount won
        :rtype: int
        """
        return int(self.amount + self.outcome.winAmount(float(self.amount)))

    def loseAmount(self) -> int:
        """
        Returns the amount bet as the amount lost. This is the cost of placing the bet.


        :return: Returns the amount bet as the amount lost. This is the cost of placing the bet.
        :rtype: int
        """
        return self.amount

    def __str__(self) -> str:
        """
        Returns a string representation of this bet. Note that this method will delegate the much of
        the work to the **__str__()** method of the :class:`Outcome`.

        :return: string representation of this bet with the form  :samp:`"{amount} on {outcome}"`
        :rtype: str
        """
        return f"{self.amount} on {self.outcome}"


class InvalidBet(Exception):
    """
    :class:`InvalidBet` is raised when a Player instance attempts to place a bet which exceeds the
    table’s limit.

    This class simply inherits all features of its superclass.
    """


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
        self.minimum = 10
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
        self.stake -= self.betMultiple

    def playing(self) -> bool:
        return super().playing() and self.betMultiple <= self.stake

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

    def playing(self) -> bool:
        return super().playing()  # pragma: no cover

    def win(self, bet: Bet) -> None:
        """
        Notification from the :class:`Game` object that the :class:`Bet` instance was a winner. The
        amount of money won is available via the **Bet.winAmount()** method.

        :param bet: The bet which won.
        """

    def lose(self, bet: Bet) -> None:
        """
        Notification from the :class:`Game` object that the :class:`Bet` instance was a loser.

        :param bet: The bet which won.
        """


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
        self.table.isValid()  # Ensures bets are valid.
        winning_bin = self.wheel.choose()
        for bet in self.table:
            if bet.outcome in winning_bin:
                player.win(bet)
            else:
                player.lose(bet)


class Simulator:
    """
    :class:`Simulator` exercises the Roulette simulation with a given :class:`Player` placing bets.
    It reports raw statistics on a number of sessions of play.

    .. attribute:: initDuration

       The duration value to use when initializing a :class:`Player` instance for a session. A
       default value of 250 is a good choice here.

    .. attribute:: initStake

       The stake value to use when initializing a :class:`Player` instance for a session. This is a
       count of the number of bets placed; i.e., 100 $10 bets is $1000 stake. A default value of 100
       is sensible.

    .. attribute:: samples

       The number of game cycles to simulate. A default value of 50 makes sense.

    .. attribute:: durations

       A **list** of lengths of time the :class:`Player` object remained in the game. Each session
       of play produces a duration metric, which are collected into this list.

    .. attribute:: maxima

       A **list** of maximum stakes for the :class:`Player` object. Each session of play produces a
       maximum stake metric, which are collected into this list.

    .. attribute:: player

       The :class:`Player` instance; essentially, the betting strategy we are simulating.

    .. attribute:: game

       The casino game we are simulating. This is an instance of the :class:`Game` class,
       which embodies the various rules, the :class:`Table` object and the :class:`Wheel` instance.
    """

    def __init__(self, game: Game, player: Player) -> None:
        """
        Saves the Player and :class:`Game` instances so we can gather statistics on the performance
        of the player’s betting strategy.

        :param game: The game we’re simulating. This includes the :class:`Table` and :class:`Wheel`.
        :param player: The player. This encapsulates the betting strategy.
        """

        self.game = game
        self.player = player
        self.initDuration = 250
        self.initStake = 100
        self.samples = 50
        self.durations: list[int] = []
        self.maxima: list[int] = []

    def session(self) -> list[int]:
        """
        :return: list of stake values.
        :rtype: list

        Executes a single game session. The :class:`Player` instance is initialized with their
        initial stake and initial cycles to go. An empty **list** of stake values is created.
        The session loop executes until the **Player.playing()** method returns false. This loop
        executes the **Game.cycle()** method; then it gets the stake from the :class:`Player` and
        appends this amount to the **list** of stake values. The **list** of individual stake
        values is returned as the result of the session of play.
        """

        self.player.stake = self.initStake
        self.player.roundsToGo = self.initDuration
        stake_values = []
        while self.player.playing():
            self.game.cycle(self.player)
            stake_values.append(self.player.stake)
            self.player.roundsToGo -= 1
        return stake_values

    def gather(self) -> None:
        """
        Executes the number of games sessions in samples. Each game session returns a **list** of
        stake values. When the session is over (either the play reached their time limit or their
        stake was spent), then the length of the session **list** and the maximum value in the
        session **list** are the resulting duration and maximum metrics. These two metrics are
        appended to the **durations** list and the **maxima** list.

        A client class will either display the durations and maxima raw metrics or produce
        statistical summaries.
        """

        for _ in range(self.samples):
            stake_values: list[int] = self.session()
            self.maxima.append(max(stake_values))
            self.durations.append(len(stake_values))
