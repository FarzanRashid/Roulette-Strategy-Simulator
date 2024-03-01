from unittest import TestCase
from table import Table

from players.player1326.player1326 import Player1326


class TestPlayer1326(TestCase):
    def setUp(self):
        self.table = Table()
        self.player1326 = Player1326(self.table)

    def test_player1326_plays_when_stake_higher_than_betAmount(self):
        self.player1326.stake = 2
        self.player1326.state.betAmount = 1
        self.assertTrue(self.player1326.playing())

        self.player1326.stake = 0

        self.assertFalse(self.player1326.playing())

    def test_player1326_plays_when_roundsToGo_more_than_zero(self):
        self.player1326.roundsToGo = 1

        self.assertTrue(self.player1326.playing())

        self.player1326.roundsToGo = 0

        self.assertFalse(self.player1326.playing())

    def test_stake_is_reduced_when_bet_placed(self):
        self.player1326.stake = 100
        self.player1326.state.betAmount = 10
        expected_bet_after_bet = 90

        self.player1326.placeBets()

        self.assertEqual(expected_bet_after_bet, self.player1326.stake)
