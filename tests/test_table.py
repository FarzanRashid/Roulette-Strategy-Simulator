from unittest import TestCase
from roulette import Table, Bet, Outcome, InvalidBet


class TestTable(TestCase):
    def setUp(self):
        self.oc1 = Outcome("Black", 1)
        self.oc2 = Outcome("1", 35)
        self.bet1 = Bet(5, self.oc1)
        self.bet2 = Bet(300, self.oc2)
        self.table = Table()

    def test_placeBet_adds_bets_to_bets_list(self):
        bet3 = Bet(30, self.oc1)
        self.table.placeBet(bet3)
        self.assertIn(bet3, self.table.bets)

    def test_isValid_raises_exception_for_bets_lower_than_minimum_bet_amount(self):
        self.table.placeBet(self.bet1)
        with self.assertRaises(InvalidBet):
            self.table.isValid()

    def test_isValid_raises_exception_when_bet_amounts_cross_table_limit(self):
        bet3 = Bet(100, self.oc1)
        self.table.placeBet(bet3)
        self.table.placeBet(self.bet2)

        with self.assertRaises(InvalidBet):
            self.table.isValid()
