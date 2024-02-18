import math


class IntegerStatistics(list):
    """
    :class:`IntegerStatistics` computes several simple descriptive statistics of int values in a
    list.

    This extends **list** with some additional methods.
    """

    def mean(self) -> float:
        """
        Computes the mean of the **List** of values.
        """

        return sum(self) / len(self)

    def stdev(self):
        mean = self.mean()
        return round(math.sqrt(sum((x-mean)**2 for x in self) / (len(self)-1)), 3)
