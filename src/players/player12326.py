from bet import Bet
from wheel import Wheel
from table import Table
from player import Player
from player1326_states import Player1326NoWin


class Player1326(Player):
    def __init__(self, table: Table, wheel: Wheel) -> None:
        super().__init__(table)
        self.table = table
        self.outcome = wheel.getOutcome("Red")
        self.state = Player1326NoWin(self)

    def playing(self) -> bool:
        return super().playing() and self.stake > 0

    def placeBets(self) -> None:
        self.table.placeBet(self.state.currentBet())

    def win(self, bet: Bet) -> None:
        super().win(bet)
        self.state = self.state.nextWon()

    def lose(self, bet: Bet) -> None:
        self.state = self.state.nextLost()
