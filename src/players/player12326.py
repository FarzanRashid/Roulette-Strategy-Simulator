from wheel import Wheel
from table import Table
from player import Player
from player1326_states import Player1326NoWin


class Player1326(Player):
    def __init__(self, table: Table, wheel: Wheel) -> None:
        self.table = table
        self.outcome = wheel.getOutcome("Red")
        
