from unittest import TestCase

from outcome import Outcome


class TestOutcome(TestCase):
    def setUp(self):
        self.oc1 = Outcome("Red", 1)
        self.oc2 = Outcome("Red", 1)
        self.oc3 = Outcome("Black", 2)

    def test_objects_with_same_name_are_equal(self):
        self.assertEqual(self.oc1, self.oc2)

    def test_same_hash_values_for_equal_objects(self):
        oc1_hash_value = hash(self.oc1)
        oc2_hash_value = hash(self.oc2)
        self.assertEqual(oc1_hash_value, oc2_hash_value)

    def test_win_amount_calculation(self):
        amount = 5
        win_amount = self.oc3.winAmount(amount)
        expected_win_amount = 10.0
        self.assertEqual(win_amount, expected_win_amount)

    def test_inequality_when_names_differ(self):
        self.assertNotEqual(self.oc1, self.oc3)
