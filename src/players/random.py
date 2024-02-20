import random

from players.player import Player


class PlayerRandom(Player):
    def __init__(self, table, wheel):
        super().__init__(table)
        self.wheel = wheel
        self.rng = random.Random()
        bin_iterator = self.wheel.binIterator()
        self.all_OC = set(outcome for bin in bin_iterator for outcome in bin)

    def placeBets(self) -> None:
        self.table.placeBet(self.rng.choice(list(self.all_OC)))
