from unittest import TestCase
from bet import Bet
from players.player1326.player1326_state import Player1326TwoWins


class TestPlayer1326TwoWins(TestCase):
    def setUp(self):
        self.player1326_two_wins = Player1326TwoWins()

    def test_only_one_instance_is_created(self):
        instance_2 = Player1326TwoWins()
        self.assertIs(self.player1326_two_wins, instance_2)

        instance_3 = Player1326TwoWins()
        self.assertIs(self.player1326_two_wins, instance_3)

    def test_currentBet_returns_bet(self):
        expected_bet = Bet(self.player1326_two_wins.betAmount, self.player1326_two_wins.outcome)
        actual_bet = self.player1326_two_wins.currentBet()

        self.assertEqual(expected_bet, actual_bet)
