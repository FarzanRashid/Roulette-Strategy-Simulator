from unittest import TestCase
from roulette import Outcome, Bet


class TestBet(TestCase):
    def setUp(self):
        self.oc1 = Outcome("Red", 1)
        self.oc2 = Outcome("35", 35)
        self.bet1 = Bet(5, self.oc1)
        self.bet2 = Bet(10, self.oc2)

    def test_winAmount_calculation(self):
        bet_one_win_amount = self.bet1.winAmount()
        bet_one_expected_win_amount = 10
        bet_two_win_amount = self.bet2.winAmount()
        bet_two_expected_win_amount = 360
        self.assertEqual(bet_one_expected_win_amount, bet_one_win_amount)
        self.assertEqual(bet_two_expected_win_amount, bet_two_win_amount)

    def test_loseAmount_calculation(self):
        bet_one_lose_amount = self.bet1.loseAmount()
        bet_two_lose_amount = self.bet2.loseAmount()
        bet_one_expected_lose_amount = self.bet1.amount
        bet_two_expected_lose_amount = self.bet2.amount
        self.assertEqual(bet_one_expected_lose_amount, bet_one_lose_amount)
        self.assertEqual(bet_two_expected_lose_amount, bet_two_lose_amount)

    def test_str_returns_amount_and_outcome(self):
        str_of_bet_one = str(self.bet1)
        str_of_bet_two = str(self.bet2)
        bet_one_expected_str = f"{self.bet1.amount} on {self.bet1.outcome}"
        bet_two_expected_str = f"{self.bet2.amount} on {self.bet2.outcome}"

        self.assertEqual(bet_one_expected_str, str_of_bet_one)
        self.assertEqual(bet_two_expected_str, str_of_bet_two)
