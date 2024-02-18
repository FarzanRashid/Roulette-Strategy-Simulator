import math

class IntegerStatistics(list):
    def mean(self):
        return sum(self) / len(self)

    def stdev(self):
        mean = self.mean()
        return round(math.sqrt(sum((x-mean)**2 for x in self) / (len(self)-1)), 3)
