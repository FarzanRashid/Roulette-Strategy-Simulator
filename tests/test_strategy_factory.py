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
