from unittest import TestCase
from roulette import Outcome, Bet


class TestBet(TestCase):
    def setUp(self):
        self.oc1 = Outcome("Red", 1)
        self.oc2 = Outcome("35", 35)
        self.bet1 = Bet(5, self.oc1)
        self.bet2 = Bet(10, self.oc2)
