from unittest import TestCase
from players.player1326.player1326_state import Player1326NoWins


class TestPlayer1326NoWins(TestCase):
    def setUp(self):
        self.player_1326_no_wins = Player1326NoWins()

    def test_only_one_instance_is_created(self):
        instance_2 = Player1326NoWins()
        self.assertIs(self.player_1326_no_wins, instance_2)

        instance_3 = Player1326NoWins()
        self.assertIs(self.player_1326_no_wins, instance_3)
