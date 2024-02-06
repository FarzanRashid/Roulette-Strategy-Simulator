from unittest import TestCase


from roulette import Simulator, Game, Martingale, Table, Wheel


class TestSimulator(TestCase):
    def setUp(self):
        self.table = Table()
        self.martingale = Martingale(self.table)
        self.wheel = Wheel()
        self.game = Game(self.wheel, self.table)
        self.simulator = Simulator(self.game, self.martingale)
