from roulette import Outcome

from unittest import TestCase


class TestOutcome(TestCase):
    def setUp(self):
        self.oc1 = Outcome("Red", 1)
        self.oc2 = Outcome("Red", 1)
        self.oc3 = Outcome("Black", 2)

    def test_equality(self):
        self.assertEquals(self.oc1, self.oc2)
