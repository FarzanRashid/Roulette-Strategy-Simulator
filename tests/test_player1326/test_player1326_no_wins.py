from unittest import TestCase
from bet import Bet
from players.player1326.player1326_state import Player1326NoWins, Player1326OneWin


class TestPlayer1326NoWins(TestCase):
    def setUp(self):
        self.player_1326_no_wins = Player1326NoWins()

    def test_only_one_instance_is_created(self):
        instance_2 = Player1326NoWins()
        self.assertIs(self.player_1326_no_wins, instance_2)

        instance_3 = Player1326NoWins()
        self.assertIs(self.player_1326_no_wins, instance_3)

    def test_currentBet_returns_bet(self):
        expected_bet = Bet(
            self.player_1326_no_wins.betAmount, self.player_1326_no_wins.outcome
        )
        actual_bet = self.player_1326_no_wins.currentBet()

        self.assertEqual(expected_bet, actual_bet)

    def test_nextWon_changes_state_to_OneWin(self):
        next_state = Player1326OneWin()
        nextWon_result = self.player_1326_no_wins.nextWon()

        self.assertIs(next_state, nextWon_result)
