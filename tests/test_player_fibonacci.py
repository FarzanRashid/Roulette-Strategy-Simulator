from unittest import TestCase
from table import Table
from bet import Bet
from players.player_fibonacci import PlayerFibonacci


class TestPlayerFibonacci(TestCase):
    def setUp(self):
        self.table = Table()
        self.player_fibonacci = PlayerFibonacci(self.table)
        self.bet = Bet(1, self.player_fibonacci.outcome)

    def test_win_resets_recent_value(self):
        self.player_fibonacci.recent = 10
        expected_recent_value_after_win = 1

        self.player_fibonacci.win(self.bet)

        self.assertEqual(self.player_fibonacci.recent, expected_recent_value_after_win)

    def test_win_resets_previous_value(self):
        self.player_fibonacci.previous = 10
        expected_previous_value_after_win = 1

        self.player_fibonacci.win(self.bet)

        self.assertEqual(self.player_fibonacci.recent, expected_previous_value_after_win)

    def test_lose_updates_bet_amount(self):
        self.player_fibonacci.bet_amount = 0
        self.player_fibonacci.recent = 1
        self.player_fibonacci.previous = 2
        expected_bet_amount_after_lose = 3

        self.player_fibonacci.lose(self.bet)

        self.assertEqual(expected_bet_amount_after_lose, self.player_fibonacci.bet_amount)

    def test_lose_updates_previous(self):
        self.player_fibonacci.previous = 0
        self.player_fibonacci.recent = 5
        expected_previous_value_after_lose = self.player_fibonacci.recent

        self.player_fibonacci.lose(self.bet)
        self.assertEqual(expected_previous_value_after_lose, self.player_fibonacci.previous)

    def test_lose_updates_recent(self):
        self.player_fibonacci.previous = 1
        self.player_fibonacci.recent = 5
        self.player_fibonacci.bet_amount = 6
        expected_recent_value_after_lose = self.player_fibonacci.bet_amount

        self.player_fibonacci.lose(self.bet)
        self.assertEqual(expected_recent_value_after_lose, self.player_fibonacci.bet_amount)

    def test_player_plays_when_stake_is_enough(self):
        self.player_fibonacci.stake = 10
        self.player_fibonacci.bet_amount = 10

        self.assertTrue(self.player_fibonacci.playing())

        self.player_fibonacci.stake = 9

        self.assertFalse(self.player_fibonacci.playing())

    def test_player_plays_when_roundsToGo_is_not_zero(self):
        self.player_fibonacci.roundsToGo = 1
        self.assertTrue(self.player_fibonacci.playing())

        self.player_fibonacci.roundsToGo = 0
        self.assertFalse(self.player_fibonacci.playing())

    def test_placeBets_places_bet(self):
        self.table.bets = []

        self.player_fibonacci.placeBets()

        self.assertIn(self.bet, self.table.bets)

    def test_placeBets_reduces_stake(self):
        self.player_fibonacci.stake = 100
        self.player_fibonacci.bet_amount = 10
        expected_stake_after_placeBets = 90

        self.player_fibonacci.placeBets()

        self.assertEqual(expected_stake_after_placeBets, self.player_fibonacci.stake)
