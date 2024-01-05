from unittest import TestCase
from roulette import Outcome, Wheel, BinBuilder


class TestBinBuilder(TestCase):
    def setUp(self):
        self.bin_builder = BinBuilder()
        self.wheel = Wheel()

    def test_if_straight_outcomes_are_generated_properly(self):
        straight_bet_odds = 35
        straight_outcomes = {
            0: Outcome("0", straight_bet_odds),
            1: Outcome("1", straight_bet_odds),
            36: Outcome("36", straight_bet_odds),
            37: Outcome("00", straight_bet_odds)
            }

        self.bin_builder.build_bins_for_straight_bets(self.wheel)

        for bin_index in straight_outcomes:
            self.assertIn(straight_outcomes[bin_index], self.wheel.bins[bin_index])

    def test_if_horizontal_split_outcomes_are_generated_properly(self):
        split_bet_odds = 17
        split_outcome_name = "1-2"
        bin_index = 1

        horizontal_split_outcome = Outcome(split_outcome_name, split_bet_odds)

        self.bin_builder.build_bins_for_horizontal_split_bets(self.wheel)

        self.assertIn(horizontal_split_outcome, self.wheel.bins[bin_index])

    def test_vertical_split_bins_are_filled_properly(self):
        split_bet_odds = 17
        split_outcome_name = "1-4"
        bin_index = 1

        vertical_split_outcome = Outcome(split_outcome_name, split_bet_odds)

        self.bin_builder.build_bins_for_vertical_split_bets(self.wheel)

        self.assertIn(vertical_split_outcome, self.wheel.bins[bin_index])

    def test_street_bins_are_filled_properly(self):
        street_bet_odds = 11
        street_outcomes = {
            1: Outcome("1-2-3", street_bet_odds),
            36: Outcome("34-35-36", street_bet_odds)
        }

        self.bin_builder.build_bins_for_street_bets(self.wheel)

        for bin_index in street_outcomes:
            self.assertIn(street_outcomes[bin_index], self.wheel.bins[bin_index])

    def test_corner_bins_are_filled_properly(self):
        corner_bet_odds = 8
        corner_outcomes = {
            1: [Outcome("1-2-4-5", corner_bet_odds)],
            4: [Outcome("1-2-4-5", corner_bet_odds), Outcome("4-5-7-8", corner_bet_odds)],
            5: [Outcome("1-2-4-5", corner_bet_odds), Outcome("4-5-7-8", corner_bet_odds),
                Outcome("2-3-5-6", corner_bet_odds), Outcome("5-6-8-9", corner_bet_odds)]
                }

        self.bin_builder.build_bins_for_corner_bets(self.wheel)

        for bin_index in corner_outcomes:
            for outcome in corner_outcomes[bin_index]:
                self.assertIn(outcome, self.wheel.bins[bin_index])

    def test_bins_are_filled_for_line_bets(self):
        line_bet_odds = 5
        line_outcomes = {
            1: [Outcome("1-2-3-4-5-6", line_bet_odds)],
            4: [Outcome("1-2-3-4-5-6", line_bet_odds), Outcome("4-5-6-7-8-9", line_bet_odds)]
        }

        self.bin_builder.build_bins_for_line_bets(self.wheel)

        for bin_index in line_outcomes:
            for outcome in line_outcomes[bin_index]:
                self.assertIn(outcome, self.wheel.bins[bin_index])
