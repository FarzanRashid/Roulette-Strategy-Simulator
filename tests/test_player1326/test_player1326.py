from unittest import TestCase
from table import Table

from players.player1326.player1326 import Player1326


class TestPlayer1326(TestCase):
    def setUp(self):
        self.table = Table()
        self.player1326 = Player1326(self.table)
