from unittest import TestCase
from roulette import Table, Bet, Outcome


class TestTable(TestCase):
    def setUp(self):
        self.oc1 = Outcome("Black", 1)
        self.oc2 = Outcome("1", 35)
        self.bet1 = Bet(5, self.oc1)
        self.bet2 = Bet(300, self.oc2)
        self.table = Table(self.bet1, self.bet2)
