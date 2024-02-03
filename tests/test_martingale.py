from unittest import TestCase

from unittest.mock import Mock, patch

from roulette import Game, Martingale, Table, Wheel, Bet, BinBuilder


class TestMartingale(TestCase):
    def setUp(self):
        self.table = Table()
        self.wheel = Wheel()
        bin_builder = BinBuilder()
        bin_builder.buildBins(self.wheel)
        self.game = Game(self.wheel, self.table)
        self.martingale = Martingale(self.table)

    def test_bets_placed_when_stake_not_less_than_betMultiple(self):
        self.martingale.stake = 10
        self.martingale.betMultiple = 15
        self.game.cycle(self.martingale)
        expected_bets_on_table = []
        actual_bets_on_table = self.table.bets
        self.assertEqual(expected_bets_on_table, actual_bets_on_table)

        self.martingale.betMultiple = 10
        bet_amount = self.martingale.betMultiple
        self.game.cycle(self.martingale)
        bet = Bet(bet_amount, self.wheel.getOutcome("Black"))
        self.assertIn(bet, self.table.bets)

    def test_stake_reduced_when_bet_placed(self):
        self.martingale.betMultiple = 10
        with patch("roulette.Wheel.choose", Mock(return_value=[])):
            self.game.cycle(self.martingale)
        expected_stake_after_bet = 90
        self.assertEqual(self.martingale.stake, expected_stake_after_bet)

    def test_stake_raised_if_bet_wins(self):
        self.martingale.betMultiple = 10
        with patch(
            "roulette.Wheel.choose", Mock(return_value=[self.wheel.getOutcome("Black")])
        ):
            self.game.cycle(self.martingale)
        expected_stake = 110
        self.assertEqual(expected_stake, self.martingale.stake)

    def test_player_plays_when_stake_not_less_than_table_minimum(self):
        self.martingale.stake = 3
        self.assertFalse(self.martingale.playing())

        self.martingale.stake = 15
        self.assertTrue(self.martingale.playing())
