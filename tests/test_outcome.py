from roulette import Outcome

from unittest import TestCase


class TestOutcome(TestCase):
    def setUp(self):
        oc1 = Outcome("Red", 1)
        oc2 = Outcome("Red", 1)
        oc3 = Outcome("Black", 2)

