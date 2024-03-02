from unittest import TestCase
from players.player1326.player1326_state import Player1326State, Player1326NoWins


class TestPlayer1326State(TestCase):
    def setUp(self):
        self.player1326_state = Player1326State()

    def test_nextLost_changes_state(self):
        no_win_state = Player1326NoWins()
        nextLost_result = self.player1326_state.nextLost()

        self.assertIs(no_win_state, nextLost_result)
