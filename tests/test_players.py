from unittest import TestCase


from roulette import Game, Martingale, Table, Wheel


class TestMartingale(TestCase):
    def setUp(self):
        self.table = Table()
        self.wheel = Wheel()
        self.game = Game(self.wheel, self.table)
        self.martingale = Martingale(self.table)
