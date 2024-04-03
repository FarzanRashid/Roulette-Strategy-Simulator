from unittest import TestCase
from table import Table
from wheel import Wheel
from bin_builder import BinBuilder
from player_factory import provide_player
from players.martingale import Martingale
from players.fibonacci import PlayerFibonacci
from players.seven_reds import SevenReds


class TestPlayerProvide(TestCase):
    def setUp(self):
        self.table = Table()
        self.wheel = Wheel()

    def test_provide_player_provides_player(self):
        bin_builder = BinBuilder()
        bin_builder.buildBins(self.wheel)

        martingale_player = provide_player("Martingale", self.table, self.wheel)

        self.assertIsInstance(martingale_player, Martingale)

        sevenreds_player = provide_player("Sevenreds", self.table, self.wheel)

        self.assertIsInstance(sevenreds_player, SevenReds)

        fibonacci_player = provide_player("Fibonacci", self.table, self.wheel)

        self.assertIsInstance(fibonacci_player, PlayerFibonacci)
