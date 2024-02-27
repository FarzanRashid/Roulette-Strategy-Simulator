from bet import Bet
from wheel import Wheel
from table import Table
from players.player import Player
from players.player1326_states import Player1326StateFactory, Player1326State


class Player1326(Player):
    def __init__(self, table: Table, wheel: Wheel) -> None:
        super().__init__(table)
        self.table = table
        self.outcome = wheel.getOutcome("Red")
        self.state: Player1326State = Player1326StateFactory(self).get("Player1326NoWins")

    def playing(self) -> bool:
        return super().playing() and self.stake > self.state.betAmount

    def placeBets(self) -> None:
        self.table.placeBet(self.state.currentBet())
        self.stake -= self.state.betAmount

    def win(self, bet: Bet) -> None:
        super().win(bet)
        self.state = self.state.nextWon()

    def lose(self, bet: Bet) -> None:
        self.state = self.state.nextLost()
