from io import StringIO
from unittest import TestCase
from unittest.mock import Mock, patch
import hw


class TestGreeting(TestCase):
    def test(self):
        g = hw.Greeting("hello", "world")
        self.assertEqual(str(g),  "hello", "world")
