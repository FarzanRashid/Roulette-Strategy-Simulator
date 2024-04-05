from unittest import TestCase
from table import Table
from wheel import Wheel
from bin_builder import BinBuilder
from player_factory import player_factory
from players.martingale import Martingale
from players.fibonacci import PlayerFibonacci
from players.seven_reds import SevenReds


class TestPlayerProvide(TestCase):
    def setUp(self):
        self.table = Table()
        self.wheel = Wheel()
        bin_builder = BinBuilder()
        bin_builder.buildBins(self.wheel)

    def test_provide_player_provides_player(self):
        martingale_player = player_factory("Martingale", self.table, self.wheel)
        self.assertIsInstance(martingale_player, Martingale)

        sevenreds_player = player_factory("Sevenreds", self.table, self.wheel)
        self.assertIsInstance(sevenreds_player, SevenReds)

        fibonacci_player = player_factory("Fibonacci", self.table, self.wheel)
        self.assertIsInstance(fibonacci_player, PlayerFibonacci)

    def test_provide_player_raise_error_when_player_name_not_valid(self):
        with self.assertRaises(ValueError):
            player_factory("Martingale123", self.table, self.wheel)

        with self.assertRaises(ValueError):
            player_factory("SevenReds01", self.table, self.wheel)

        with self.assertRaises(ValueError):
            player_factory("FIBONACCI789", self.table, self.wheel)
