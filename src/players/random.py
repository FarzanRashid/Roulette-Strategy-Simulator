import random
from bet import Bet
from players.player import Player


class PlayerRandom(Player):
    """
    :class:`PlayerRandom` is a :py:class:`~players.player.Player` who places bets in Roulette.
    This player makes random bets around the layout.
    """

    def __init__(self, table, wheel):
        super().__init__(table)
        self.wheel = wheel
        self.rng = random.Random()
        bin_iterator = self.wheel.binIterator()
        self.all_OC = set(outcome for bin in bin_iterator for outcome in bin)

    def placeBets(self) -> None:
        self.table.placeBet(Bet(1, self.rng.choice(list(self.all_OC))))
