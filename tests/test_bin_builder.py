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
