from unittest import TestCase

from integer_statistics import IntegerStatistics


class TestIntegerStatistics(TestCase):
    def setUp(self):
        int_stat = IntegerStatistics([10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5])
