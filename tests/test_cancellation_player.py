from unittest import TestCase
from table import Table
from bet import Bet
from outcome import Outcome
from players.cancellation_player import PlayerCancellation


class TestPlayerCancellation(TestCase):
    def setUp(self):
        self.table = Table()
        self.player_cancellation = PlayerCancellation(self.table)

    def test_resetSequence_resets_sequence(self):
        self.player_cancellation.sequence = []
        expected_seq_after_resetSequence = [1, 2, 3, 4, 5, 6]
        self.player_cancellation.resetSequence()
        self.assertEqual(
            self.player_cancellation.sequence, expected_seq_after_resetSequence
        )

    def test_lose_adds_bet_amount_to_sequence(self):
        bet = Bet(10, Outcome("Red", 1))
        self.assertNotIn(bet.amount, self.player_cancellation.sequence)

        self.player_cancellation.lose(bet)
        self.assertIn(bet.amount, self.player_cancellation.sequence)

    def test_win_removes_elements_from_sequence(self):
        bet = Bet(7, Outcome("Red", 1))
        expected_seq_before_win = [1, 2, 3, 4, 5, 6]
        self.assertEqual(expected_seq_before_win, self.player_cancellation.sequence)

        expected_seq_after_win = [2, 3, 4, 5]

        self.player_cancellation.win(bet)

        self.assertEqual(expected_seq_after_win, self.player_cancellation.sequence)

    def test_placeBets_reduces_stake(self):
        self.player_cancellation.stake = 100
        expected_stake_after_bet = 93

        self.player_cancellation.placeBets()
        self.assertIs(self.player_cancellation.stake, expected_stake_after_bet)

    def test_placeBets_places_bet(self):
        bets_on_table_before_placeBets = []
        self.assertEqual(bets_on_table_before_placeBets, self.table.bets)

        expected_bet_in_table_after_placeBets = Bet(7, Outcome("Red", 1))

        self.player_cancellation.placeBets()

        self.assertIn(expected_bet_in_table_after_placeBets, self.table.bets)

    def test_player_plays_when_stake_more_than_bet_amount(self):
        self.player_cancellation.bet_amount = 9

        self.player_cancellation.stake = 10
        self.assertTrue(self.player_cancellation.playing())

        self.player_cancellation.stake = 8
        self.assertFalse(self.player_cancellation.playing())

    def test_player_plays_when_roundstoGo_not_zero(self):
        self.player_cancellation.roundsToGo = 1
        self.assertTrue(self.player_cancellation.playing())

        self.player_cancellation.roundsToGo = 0

        self.assertFalse(self.player_cancellation.playing())

    def test_player_plays_when_have_enough_sequence(self):
        self.player_cancellation.sequence = [1, 2, 3]
        self.assertTrue(self.player_cancellation.playing())

        self.player_cancellation.sequence = [1]
        self.assertFalse(self.player_cancellation.playing())

    def test_playing_resets_sequence_if_player_not_playing(self):
        self.player_cancellation.sequence = []
        self.player_cancellation.stake = 0
        expected_sequence_after_playing = [1, 2, 3, 4, 5, 6]

        self.player_cancellation.playing()
        self.assertEqual(
            expected_sequence_after_playing, self.player_cancellation.sequence
        )
