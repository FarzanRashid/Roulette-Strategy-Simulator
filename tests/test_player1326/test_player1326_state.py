from unittest import TestCase
from players.player1326.player1326_state import Player1326State, Player1326NoWins


class TestPlayer1326State(TestCase):
    def setUp(self):
        self.player1326_state = Player1326State()

    def test_nextLost_changes_state(self):
        no_win_state = Player1326NoWins()
        nextLost_result = self.player1326_state.nextLost()

        self.assertIs(no_win_state, nextLost_result)

    def test_currentBet_returns_NoImplemented(self):
        expected_currentBet_result = NotImplemented
        actual_currentBet_result = self.player1326_state.currentBet()

        self.assertIs(expected_currentBet_result, actual_currentBet_result)

    def test_NextWon_returns_NoImplemented(self):
        expected_nextWon_result = NotImplemented
        actual_nextWon_result = self.player1326_state.nextWon()

        self.assertIs(expected_nextWon_result, actual_nextWon_result)
