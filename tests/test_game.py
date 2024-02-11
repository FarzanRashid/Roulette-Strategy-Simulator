from unittest import TestCase

from unittest.mock import Mock, patch

from game import Game
from wheel import Wheel
from table import Table
from bin_builder import BinBuilder
from invalid_bet import InvalidBet
from players.passenger57 import Passenger57


class TestGame(TestCase):
    def setUp(self):
        self.wheel = Wheel()
        self.table = Table()
        bin_builder = BinBuilder()
        bin_builder.buildBins(self.wheel)
        self.game = Game(self.wheel, self.table)
        self.passenger = Passenger57(self.table, self.wheel)

    def test_cycle_calls_placeBets(self):
        place_bets_mock = Mock(name="place_bets_mock")
        with patch("roulette.Passenger57.placeBets", place_bets_mock):
            self.game.cycle(self.passenger)
        place_bets_mock.assert_called_once()

    def test_cycle_calls_choose(self):
        choose_mock = Mock(name="choose_mock", return_value=[])
        with patch("roulette.Wheel.choose", choose_mock):
            self.game.cycle(self.passenger)
        choose_mock.assert_called_once()

    def test_cycle_calls_win_if_bet_wins(self):
        winning_outcome = self.wheel.getOutcome("Black")
        choose_mock = Mock(name="choose_mock", return_value=[winning_outcome])
        win_mock = Mock(name="win_mock")
        with patch("roulette.Wheel.choose", choose_mock):
            with patch("roulette.Passenger57.win", win_mock):
                self.game.cycle(self.passenger)
        win_mock.assert_called_once()

    def test_cycle_calls_lose_if_bet_loses(self):
        winning_outcome = self.wheel.getOutcome("Red")
        choose_mock = Mock(name="choose_mock", return_value=[winning_outcome])
        lose_mock = Mock(name="lose_mock")
        with patch("roulette.Wheel.choose", choose_mock):
            with patch("roulette.Passenger57.lose", lose_mock):
                self.game.cycle(self.passenger)
        lose_mock.assert_called_once()

    def test_choose_not_called_if_isValid_raises_exception(self):
        place_bets_mock = Mock(name="place_bets_mock", side_effect=InvalidBet)
        choose_mock = Mock(name="choose_mock")
        with patch("roulette.Passenger57.placeBets", place_bets_mock):
            with patch("roulette.Wheel.choose", choose_mock):
                with self.assertRaises(InvalidBet):
                    self.game.cycle(self.passenger)
        choose_mock.assert_not_called()
