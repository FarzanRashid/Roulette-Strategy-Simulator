from players.player1326.player1326_no_wins import Player1326NoWins
from players.player1326.player1326_one_win import Player1326OneWin
from players.player1326.player1326_state import Player1326State
from players.player1326.player1326_two_wins import Player1326TwoWins
from players.player1326.player1326_three_wins import Player1326ThreeWins


class Player1326StateFactory:
    def __init__(self) -> None:
        self.values = {"Player1326NoWins": Player1326NoWins(),
                       "Player1326OneWin": Player1326OneWin(),
                       "Player1326TwoWins": Player1326TwoWins(),
                       "Player1326ThreeWins": Player1326ThreeWins(),
                       }

    def get(self, name: str) -> Player1326State:
        return self.values[name]
