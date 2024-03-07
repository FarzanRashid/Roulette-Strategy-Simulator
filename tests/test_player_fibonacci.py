from unittest import TestCase
from table import Table
from bet import Bet
from players.player_fibonacci import PlayerFibonacci


class TestPlayerFibonacci(TestCase):
    def setUp(self):
        self.table = Table()
        self.player_fibonacci = PlayerFibonacci(self.table)
        self.bet = Bet(1, self.player_fibonacci.outcome)

    def test_win_resets_recent_value(self):
        self.player_fibonacci.recent = 10
        expected_recent_value_after_win = 1

        self.player_fibonacci.win(self.bet)

        self.assertEqual(self.player_fibonacci.recent, expected_recent_value_after_win)
