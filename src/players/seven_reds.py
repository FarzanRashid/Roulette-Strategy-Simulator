from .martingale import Martingale


class SevenReds(Martingale):
    def __init__(self, table):
        super().__init__(table)
        self.redCount = 7

    def placeBets(self) -> None:
        if self.redCount == 0:
            super().placeBets()
