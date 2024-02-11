from outcome import Outcome
from wheel import Wheel


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
