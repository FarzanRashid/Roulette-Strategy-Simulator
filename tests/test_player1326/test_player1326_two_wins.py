from unittest import TestCase

from players.player1326.player1326_state import Player1326TwoWins


class TestPlayer1326TwoWins(TestCase):
    def setUp(self):
        self.player1326_two_wins = Player1326TwoWins()

    def test_only_one_instance_is_created(self):
        instance_2 = Player1326TwoWins()
        self.assertIs(self.player1326_two_wins, instance_2)

        instance_3 = Player1326TwoWins()
        self.assertIs(self.player1326_two_wins, instance_3)
