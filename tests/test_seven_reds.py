from unittest import TestCase
from players.seven_reds import SevenReds
from table import Table


class TestSevenReds(TestCase):
    def setUp(self):
        self.table = Table()
        self.seven_reds = SevenReds(self.table)
