from unittest import TestCase
from wheel import Wheel
from table import Table
from players.random import PlayerRandom


class TestRandom(TestCase):
    def setUp(self):
        wheel = Wheel()
        table = Table()
        self.random_player = PlayerRandom(table, wheel)
