from unittest import TestCase
from table import Table
from players.cancellation_player import PlayerCancellation


class TestPlayerCancellation(TestCase):
    def setUp(self):
        self.table = Table()
        self.player_cancellation = PlayerCancellation(self.table)
