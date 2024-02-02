from unittest import TestCase

from roulette import Game, Martingale, Table, Wheel, Bet, Outcome


class TestMartingale(TestCase):
    def setUp(self):
        self.table = Table()
        self.wheel = Wheel()
        self.game = Game(self.wheel, self.table)
        self.martingale = Martingale(self.table)

    def test_placeBets_make_bets_if_enough_stake(self):
        self.martingale.betMultiple = 10
        bet_amount = self.martingale.betMultiple
        self.game.cycle(self.martingale)
        bet = Bet(bet_amount, Outcome("Black", 1))
        self.assertIn(bet, self.table.bets)

    def test_placeBets_dont_make_bets_if_stake_not_enough(self):
        self.martingale.stake = 10
        self.martingale.betMultiple = 15
        self.game.cycle(self.martingale)
        expected_bets_on_table = []
        actual_bets_on_table = self.table.bets
        self.assertEqual(expected_bets_on_table, actual_bets_on_table)
