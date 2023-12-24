from unittest import TestCase
from roulette import Outcome, Bin, Wheel


class TestWheel(TestCase):
    def setUp(self):
        self.oc1 = Outcome("Red", 1)
        self.oc2 = Outcome("Black", 2)
        self.b1 = Bin([self.oc1, self.oc2])
        self.b2 = Bin([self.oc2, self.oc2])
        self.wheel = Wheel()
