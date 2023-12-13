from roulette import Outcome

from unittest import TestCase


class TestOutcome(TestCase):
    def setUp(self):
        self.oc1 = Outcome("Red", 1)
        self.oc2 = Outcome("Red", 1)
        self.oc3 = Outcome("Black", 2)

    def test_equality(self):
        self.assertEquals(self.oc1, self.oc2)

    def test_same_hash_values_for_equal_objects(self):
        oc1_hash_value = self.oc1.__hash__()
        oc2_hash_value = self.oc2.__hash__()
        self.assertEquals(oc1_hash_value, oc2_hash_value)

    def test_winAmount_method(self):
        oc3_winamount_value = self.oc3.winAmount(5)
        self.assertEquals(oc3_winamount_value, 10.0)
