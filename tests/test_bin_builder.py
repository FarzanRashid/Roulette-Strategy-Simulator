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
