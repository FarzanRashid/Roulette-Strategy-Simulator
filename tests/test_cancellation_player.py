from unittest import TestCase
from table import Table
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
