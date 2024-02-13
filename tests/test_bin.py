from unittest import TestCase
from bin import Bin
from outcome import Outcome


class TestBin(TestCase):
    def setUp(self):
        self.oc1 = Outcome("Red", 1)
        self.oc2 = Outcome("Black", 2)

    def test_bin_objects_can_be_created_with_outcome_objects(self):
        b1 = Bin([self.oc1, self.oc2])
        b2 = Bin([self.oc2, self.oc2])
        self.assertTrue(isinstance(b1, Bin), "b1 should be a object of Bin class")
        self.assertTrue(isinstance(b2, Bin), "b2 should be a object of Bin class")
