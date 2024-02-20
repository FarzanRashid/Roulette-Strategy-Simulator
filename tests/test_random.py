from unittest import TestCase
from wheel import Wheel
from table import Table
from bin_builder import BinBuilder
from players.random import PlayerRandom


class TestRandom(TestCase):
    def setUp(self):
        self.wheel = Wheel()
        table = Table()
        bin_builder = BinBuilder()
        bin_builder.buildBins(self.wheel)
        self.random_player = PlayerRandom(table, self.wheel)

    def test_all_outcomes_are_added_to_all_OC(self):
        all_outcomes = {outcome for outcome in self.wheel.all_outcomes.values()}

        self.assertEqual(all_outcomes, self.random_player.all_OC)
