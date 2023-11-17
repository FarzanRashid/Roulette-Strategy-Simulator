from io import StringIO
from unittest.mock import Mock
import pytest
import hw


def test_greeting():
    g = hw.Greeting("x", "y")
    assert str(g) == "x y"
