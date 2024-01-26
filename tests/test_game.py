from unittest import TestCase

from unittest.mock import Mock, patch

from roulette import Wheel, Table, Passenger57, Game, BinBuilder


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
