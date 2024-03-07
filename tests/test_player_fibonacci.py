from unittest import TestCase
from table import Table
from players.player_fibonacci import PlayerFibonacci


class TestPlayerFibonacci(TestCase):
    def setUp(self):
        self.table = Table()
        self.player_fibonacci = PlayerFibonacci(self.table)
