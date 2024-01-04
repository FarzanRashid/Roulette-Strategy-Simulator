from unittest import TestCase
from roulette import Outcome, Wheel, BinBuilder


class TestBinBuilder(TestCase):
    def setUp(self):
        self.bin_builder = BinBuilder()
        self.wheel = Wheel()
