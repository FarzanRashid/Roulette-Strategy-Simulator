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
        all_outcomes = {outcome for outcome in self.wheel.all_outcomes.values()}

        self.assertEqual(all_outcomes, self.random_player.all_OC)

    def test_placeBets_bets_on_randomly_selected_outcome_with_seed(self):
        self.random_player.all_OC = list(self.random_player.all_OC)
        fixed_seed = 1
        self.random_player.rng.seed(fixed_seed)
        radomly_selected_outcome = self.random_player.rng.choice(self.random_player.all_OC)
        self.random_player.placeBets()
        self.assertIn(radomly_selected_outcome, self.table.bets)
