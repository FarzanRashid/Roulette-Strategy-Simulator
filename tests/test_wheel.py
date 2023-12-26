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

    def test_outcome_objects_can_be_added_to_bin_objects(self):
        bin_number = 0
        self.wheel.addOutcome(bin_number, self.oc1)
        self.assertIn(self.oc1, self.wheel.bins[0])

    def test_choose_returns_random_bin_object(self):
        random_bin = self.wheel.choose()
        self.assertIn(random_bin, self.wheel.bins)

    def test_get_returns_specific_bin_object(self):
        bin_object_index = 1

        selected_bin_object = self.wheel.get(bin_object_index)
        object_at_specific_index = self.wheel.bins[bin_object_index]

        self.assertEqual(selected_bin_object, object_at_specific_index)

    def test_choose_returns_random_bin_object_with_seed(self):
        fixed_seed_for_random_object = 1
        bin_number = 8

        self.wheel.rng.seed(fixed_seed_for_random_object)
        self.wheel.addOutcome(bin_number, self.oc1)

        randomly_selected_bin_object = self.wheel.choose()

        self.assertIn(self.oc1, randomly_selected_bin_object)
