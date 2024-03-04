from unittest import TestCase
from bet import Bet
from players.player1326.player1326_state import Player1326ThreeWins, Player1326NoWins


class TestPlayer1326ThreeWins(TestCase):
    def setUp(self):
        self.player1326_three_wins = Player1326ThreeWins()

    def test_only_one_instance_is_created(self):
        instance_2 = Player1326ThreeWins()
        self.assertIs(self.player1326_three_wins, instance_2)

        instance_3 = Player1326ThreeWins()
        self.assertIs(self.player1326_three_wins, instance_3)

    def test_currentBet_returns_bet(self):
        expected_bet = Bet(
            self.player1326_three_wins.betAmount, self.player1326_three_wins.outcome
        )
        actual_bet = self.player1326_three_wins.currentBet()

        self.assertEqual(expected_bet, actual_bet)

    def test_nextWon_changes_state_to_NoWins(self):
        next_state = Player1326NoWins()
        nextWon_result = self.player1326_three_wins.nextWon()
        self.assertIs(next_state, nextWon_result)
