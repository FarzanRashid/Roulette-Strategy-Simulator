from io import StringIO
from unittest import TestCase
from unittest.mock import Mock, patch
import hw


class TestGreeting(TestCase):
    def test(self):
        g = hw.Greeting("hello", "world")
        self.assertEqual(str(g), "hello world")


class TestMain(TestCase):
    def setUp(self):
        self.mock_greeting = Mock(
            name='Greeting', return_value=Mock(
                name="Greeting instance",
                __str__=Mock(return_value="mock str output")))
        self.mock_stdout = StringIO()

    def test(self):
        with patch("hw.Greeting", self.mock_greeting):
            with patch("sys.stdout", self.mock_stdout):
                hw.main()

        self.mock_greeting.assert_called()
        self.mock_greeting.return_value.__str__.assert_called_with()
        self.assertEqual("mock str output\n", self.mock_stdout.getvalue())
