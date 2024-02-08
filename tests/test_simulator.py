from unittest import TestCase

from unittest.mock import Mock, patch

from roulette import Simulator, Game, Martingale, Table, Wheel, InvalidBet


class TestSimulator(TestCase):
    def setUp(self):
        table = Table()
        self.martingale = Martingale(table)
        wheel = Wheel()
        game = Game(wheel, table)
        self.simulator = Simulator(game, self.martingale)

    def test_simulator_gathers_max_stake(self):
        session_mock = Mock(name="session_mock", return_value=[1, 2, 5])
        self.simulator.samples = 1

        with patch("roulette.Simulator.session", session_mock):
            self.simulator.gather()

        session_mock.assert_called_once()

        expected_value_in_maxima = 5
        self.assertIn(expected_value_in_maxima, self.simulator.maxima)

    def test_simulator_gathers_session_duration(self):
        session_mock = Mock(name="session_mock", return_value=[1, 2, 5])
        self.simulator.samples = 1

        with patch("roulette.Simulator.session", session_mock):
            self.simulator.gather()

        session_mock.assert_called_once()

        expected_length_in_duration = 3
        self.assertIn(expected_length_in_duration, self.simulator.durations)

    def test_session_gathers_list_of_stake(self):
        cycle_mock = Mock(name="cycle_mock")
        with patch("roulette.Game.cycle", cycle_mock):
            session_result = self.simulator.session()

        self.assertTrue(len(session_result) > 0)

    def test_exceptions_is_handled_in_placeBets(self):
        self.martingale.betMultiple = 500
        with self.assertRaises(InvalidBet):
            self.martingale.placeBets()

        expected_losscount_value = 0
        expected_betmultiple_value = 2**expected_losscount_value

        self.assertEqual(expected_losscount_value, self.martingale.losscount)
        self.assertEqual(expected_betmultiple_value, self.martingale.betMultiple)
