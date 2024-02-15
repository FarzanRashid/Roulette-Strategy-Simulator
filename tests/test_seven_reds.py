from unittest import TestCase
from table import Table
from bet import Bet
from outcome import Outcome
from players.seven_reds import SevenReds


class TestSevenReds(TestCase):
    def setUp(self):
        self.table = Table()
        self.seven_reds = SevenReds(self.table)

    def test_bet_placed_if_redCount_is_zero(self):
        self.seven_reds.redCount = 7
        expected_bet_in_table = []
        self.seven_reds.placeBets()

        self.assertEqual(expected_bet_in_table, self.table.bets)

        self.seven_reds.redCount = 0
        self.seven_reds.placeBets()

        expected_bet_in_table = Bet(1, Outcome("Black", 1))

        self.assertIn(expected_bet_in_table, self.table.bets)
