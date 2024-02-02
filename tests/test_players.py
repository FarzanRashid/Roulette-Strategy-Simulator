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
