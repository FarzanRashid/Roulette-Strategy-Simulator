from unittest import TestCase

from unittest.mock import Mock, patch

from game import Game
from table import Table
from bet import Bet
from bin_builder import BinBuilder
from invalid_bet import InvalidBet
from wheel import Wheel
from players.martingale import Martingale


class TestMartingale(TestCase):
    def setUp(self):
        self.table = Table()
        self.wheel = Wheel()
        bin_builder = BinBuilder()
        bin_builder.buildBins(self.wheel)
        self.game = Game(self.wheel, self.table)
        self.martingale = Martingale(self.table)

    def test_bets_placed_when_player_is_playing(self):
        self.martingale.stake = 10
        self.martingale.betMultiple = 15

        self.assertFalse(self.martingale.playing())

        expected_bets_on_table = []
        actual_bets_on_table = self.table.bets
        self.assertEqual(expected_bets_on_table, actual_bets_on_table)

        self.martingale.betMultiple = 10

        self.assertTrue(self.martingale.playing())

        bet_amount = self.martingale.betMultiple
        self.game.cycle(self.martingale)
        bet = Bet(bet_amount, self.wheel.getOutcome("Black"))
        self.assertIn(bet, self.table.bets)

    def test_stake_reduced_when_bet_placed(self):
        self.martingale.betMultiple = 10
        with patch("wheel.Wheel.choose", Mock(return_value=[])):
            self.game.cycle(self.martingale)
        expected_stake_after_bet = 90
        self.assertEqual(self.martingale.stake, expected_stake_after_bet)

    def test_stake_raised_if_bet_wins(self):
        self.martingale.betMultiple = 10
        with patch(
            "wheel.Wheel.choose", Mock(return_value=[self.wheel.getOutcome("Black")])
        ):
            self.game.cycle(self.martingale)
        expected_stake = 110
        self.assertEqual(expected_stake, self.martingale.stake)

    def test_player_plays_when_stake_not_less_than_table_minimum(self):
        self.martingale.stake = 0
        self.assertFalse(self.martingale.playing())

        self.martingale.stake = 15
        self.assertTrue(self.martingale.playing())

    def test_player_plays_if_rounds_are_more_than_zero(self):
        self.assertTrue(self.martingale.playing())

        self.martingale.roundsToGo = 0

        self.assertFalse(self.martingale.playing())

    def test_attributes_are_reset_if_invalid_bet_is_placed(self):
        self.martingale.betMultiple = 500
        with self.assertRaises(InvalidBet):
            self.martingale.placeBets()

        expected_losscount_value = 0
        expected_betmultiple_value = 2**expected_losscount_value

        self.assertEqual(expected_losscount_value, self.martingale.losscount)
        self.assertEqual(expected_betmultiple_value, self.martingale.betMultiple)
