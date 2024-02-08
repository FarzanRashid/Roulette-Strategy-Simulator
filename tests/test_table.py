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
        invalid_bet = Bet(0, self.oc1)
        self.table.placeBet(invalid_bet)
        with self.assertRaises(InvalidBet):
            self.table.isValid()

    def test_isValid_raises_exception_when_bet_amounts_cross_table_limit(self):
        bet3 = Bet(100, self.oc1)
        self.table.placeBet(bet3)
        self.table.placeBet(self.bet2)

        with self.assertRaises(InvalidBet):
            self.table.isValid()

    def test_iter_returns_iterator_of_bets(self):
        empty_list_iterator = iter(self.table)
        self.assertEqual([], list(empty_list_iterator))

        self.table.placeBet(self.bet1)
        self.table.placeBet(self.bet2)

        bets_iterator = iter(self.table)

        for bet in bets_iterator:
            self.assertIn(bet, self.table.bets)
            self.assertIsInstance(bet, Bet)

    def test_str_returns_current_bets(self):
        empty_bets_str_result = str(self.table)
        expected_result_with_no_bets = "No current bets"
        self.assertEqual(expected_result_with_no_bets, empty_bets_str_result)

        self.table.placeBet(self.bet1)
        self.table.placeBet(self.bet2)

        str_result_with_bets = str(self.table)

        bet_strings = [
            str(self.bet1),
            str(self.bet2),
        ]
        expected_result_with_bets = "Current bets: \n:" + "\n".join(bet_strings)

        self.assertEqual(expected_result_with_bets, str_result_with_bets)

    def test_repr_returns_current_bets(self):
        empty_bets_repr_result = repr(self.table)
        expected_result_with_no_bets = "Table()"

        self.assertEqual(expected_result_with_no_bets, empty_bets_repr_result)

        self.table.placeBet(self.bet1)
        self.table.placeBet(self.bet2)

        repr_result_with_bets = repr(self.table)
        repr_string = ", ".join(repr(bet) for bet in self.table.bets)

        expected_result_with_bets = f"Table({repr_string})"

        self.assertEqual(expected_result_with_bets, repr_result_with_bets)
