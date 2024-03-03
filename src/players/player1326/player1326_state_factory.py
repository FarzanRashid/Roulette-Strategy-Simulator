from players.player1326.player1326_state import Player1326State, Player1326NoWins, Player1326OneWin
from players.player1326.player1326_state import Player1326TwoWins, Player1326ThreeWins


class Player1326StateFactory:
    """
    .. attribute:: values

    This is a map from a class name to an object instance.
    """

    def __init__(self) -> None:
        self.values = {"Player1326NoWins": Player1326NoWins(),
                       "Player1326OneWin": Player1326OneWin(),
                       "Player1326TwoWins": Player1326TwoWins(),
                       "Player1326ThreeWins": Player1326ThreeWins(),
                       }

    def get(self, name: str) -> Player1326State:
        return self.values[name]
