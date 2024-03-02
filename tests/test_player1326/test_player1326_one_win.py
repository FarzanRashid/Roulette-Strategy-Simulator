from unittest import TestCase
from bet import Bet
from players.player1326.player1326_state import Player1326OneWin


class TestPlayer1326OneWin(TestCase):
    def setUp(self):
        self.player1326_one_win = Player1326OneWin()

    def test_only_one_instance_is_created(self):
        instance_2 = Player1326OneWin()
        self.assertIs(self.player1326_one_win, instance_2)

        instance_3 = Player1326OneWin()
        self.assertIs(self.player1326_one_win, instance_3)

    def test_currentBet_returns_bet(self):
        expected_bet = Bet(self.player1326_one_win.betAmount, self.player1326_one_win.outcome)
        actual_bet = self.player1326_one_win.currentBet()

        self.assertEqual(expected_bet, actual_bet)
