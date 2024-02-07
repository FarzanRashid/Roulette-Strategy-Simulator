from unittest import TestCase

from unittest.mock import Mock, patch

from roulette import Simulator, Game, Martingale, Table, Wheel


class TestSimulator(TestCase):
    def setUp(self):
        table = Table()
        martingale = Martingale(table)
        wheel = Wheel()
        game = Game(wheel, table)
        self.simulator = Simulator(game, martingale)

    def test_gather_appends_max_stake_and_rounds_played_after_one_session(self):
        session_mock = Mock(name="session_mock", return_value=[1, 2, 5])
        self.simulator.samples = 1

        with patch("roulette.Simulator.session", session_mock):
            self.simulator.gather()

        session_mock.assert_called_once()

        expected_value_in_maxima = 5
        self.assertIn(expected_value_in_maxima, self.simulator.maxima)

        expected_length_in_duration = 3
        self.assertIn(expected_length_in_duration, self.simulator.durations)

    def test_session_calls_cycle_only_if_players_are_active(self):
        cycle_mock = Mock(name="cycle_mock")

        playing_mock = Mock(name="playing_mock", return_value=False)

        with patch("roulette.Martingale.playing", playing_mock):
            self.simulator.session()

        cycle_mock.assert_not_called()

        with patch("roulette.Game.cycle", cycle_mock):
            self.simulator.session()
        cycle_mock.assert_called()

    def test_session_gathers_list_of_stake(self):
        cycle_mock = Mock(name="cycle_mock")
        with patch("roulette.Game.cycle", cycle_mock):
            session_result = self.simulator.session()

        self.assertTrue(len(session_result) > 0)
