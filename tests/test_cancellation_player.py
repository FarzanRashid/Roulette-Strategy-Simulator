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
        self.assertEqual(self.player_cancellation.sequence, expected_seq_after_resetSequence)

    def test_lose_adds_bet_amount_to_sequence(self):
        bet = Bet(10, Outcome("Red", 1))
        self.assertNotIn(bet.amount, self.player_cancellation.sequence)

        self.player_cancellation.lose(bet)
        self.assertIn(bet.amount, self.player_cancellation.sequence)
