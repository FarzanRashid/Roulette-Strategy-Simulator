from .martingale import Martingale


class SevenReds(Martingale):
    def __init__(self, table):
        super().__init__(table)
        self.redCount = 7
