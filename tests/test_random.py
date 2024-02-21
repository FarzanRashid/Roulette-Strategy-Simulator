from unittest import TestCase
from wheel import Wheel
from table import Table
from bin_builder import BinBuilder
from players.random import PlayerRandom


class TestRandom(TestCase):
    def setUp(self):
        self.wheel = Wheel()
        self.table = Table()
        bin_builder = BinBuilder()
        bin_builder.buildBins(self.wheel)
        self.random_player = PlayerRandom(self.table, self.wheel)

    def test_all_outcomes_are_added_to_all_OC(self):
        all_outcomes = set(self.wheel.all_outcomes.values())

        self.assertEqual(all_outcomes, self.random_player.all_OC)

    def test_bets_on_randomly_selected_outcome_with_seed(self):
        fixed_seed = 1
        self.random_player.rng.seed(fixed_seed)
        randomly_selected_outcome = self.random_player.rng.choice(
            list(self.random_player.all_OC)
        )
        self.random_player.rng.seed(fixed_seed)
        self.random_player.placeBets()
        self.assertEqual(randomly_selected_outcome, self.table.bets[0].outcome)
