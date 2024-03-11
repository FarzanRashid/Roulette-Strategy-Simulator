from unittest import TestCase
from table import Table
from bet import Bet
from outcome import Outcome
from players.cancellation import PlayerCancellation


class TestPlayerCancellation(TestCase):
    def setUp(self):
        self.table = Table()
        self.player_cancellation = PlayerCancellation(self.table)

    def test_sequence_is_reset(self):
        self.player_cancellation.sequence = []
        expected_sequence = [1, 2, 3, 4, 5, 6]
        self.player_cancellation.resetSequence()
        self.assertEqual(self.player_cancellation.sequence, expected_sequence)

    def test_bet_amount_added_to_sequence_after_lose(self):
        bet = Bet(10, Outcome("Red", 1))
        self.assertNotIn(bet.amount, self.player_cancellation.sequence)

        self.player_cancellation.lose(bet)
        self.assertIn(bet.amount, self.player_cancellation.sequence)

    def test_elements_are_removed_from_sequence(self):
        bet = Bet(7, Outcome("Red", 1))
        expected_sequence = [1, 2, 3, 4, 5, 6]
        self.assertEqual(expected_sequence, self.player_cancellation.sequence)

        expected_seq_after_win = [2, 3, 4, 5]

        self.player_cancellation.win(bet)

        self.assertEqual(expected_seq_after_win, self.player_cancellation.sequence)

    def test_placing_bet_reduces_stake(self):
        self.player_cancellation.stake = 100
        expected_stake = 93

        self.player_cancellation.placeBets()
        self.assertIs(self.player_cancellation.stake, expected_stake)

    def test_bets_are_placed(self):
        bets_on_table = []
        self.assertEqual(bets_on_table, self.table.bets)

        expected_bet_on_table = Bet(7, Outcome("Red", 1))

        self.player_cancellation.placeBets()

        self.assertIn(expected_bet_on_table, self.table.bets)

    def test_player_plays_when_stake_more_than_bet_amount(self):
        self.player_cancellation.bet_amount = 9

        self.player_cancellation.stake = 10
        self.assertTrue(self.player_cancellation.playing())

        self.player_cancellation.stake = 8
        self.assertFalse(self.player_cancellation.playing())

    def test_player_plays_when_rounds_remaining(self):
        self.player_cancellation.roundsToGo = 1
        self.assertTrue(self.player_cancellation.playing())

        self.player_cancellation.roundsToGo = 0

        self.assertFalse(self.player_cancellation.playing())

    def test_player_plays_when_have_enough_sequence(self):
        self.player_cancellation.sequence = [1, 2, 3]
        self.assertTrue(self.player_cancellation.playing())

        self.player_cancellation.sequence = [1]
        self.assertFalse(self.player_cancellation.playing())

    def test_sequence_is_reset_when_player_is_not_playing(self):
        self.player_cancellation.sequence = []
        expected_sequence_after_playing = [1, 2, 3, 4, 5, 6]

        self.assertFalse(self.player_cancellation.playing())
        self.assertEqual(
            expected_sequence_after_playing, self.player_cancellation.sequence
        )
