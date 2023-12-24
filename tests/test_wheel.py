from unittest import TestCase
from roulette import Outcome, Bin, Wheel


class TestWheel(TestCase):
    def setUp(self):
        self.oc1 = Outcome("Red", 1)
        self.oc2 = Outcome("Black", 2)
        self.b1 = Bin([self.oc1, self.oc2])
        self.b2 = Bin([self.oc2, self.oc2])
        self.wheel = Wheel()

    def test_bin_objects_can_be_added_to_wheel_class(self):
        expected_bins_length = 38
        wheel_bins_length = len(self.wheel.bins)
        self.assertEqual(wheel_bins_length, expected_bins_length)
