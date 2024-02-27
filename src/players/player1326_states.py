from abc import abstractmethod
from bet import Bet
from players.player import Player


class Player1326ThreeWins(Player1326State):
    _player1326_three_wins = None

    def __init__(self, player: Player) -> None:
        super().__init__(player)
        self.betAmount = 6

    def __new__(cls, *args, **kwargs) -> "Player1326ThreeWins":
        if cls._player1326_three_wins is None:
            cls._player1326_three_wins = super().__new__(cls)
        return cls._player1326_three_wins

    def currentBet(self) -> Bet:
        return Bet(self.betAmount, self.player.outcome)

    def nextWon(self) -> Player1326State:
        return Player1326NoWins(self.player)


class Player1326StateFactory:
    def __init__(self, player: Player) -> None:
        self.values = {"Player1326NoWins": Player1326NoWins(player),
                       "Player1326OneWin": Player1326OneWin(player),
                       "Player1326TwoWins": Player1326TwoWins(player),
                       "Player1326ThreeWins": Player1326ThreeWins(player),
                       }

    def get(self, name: str) -> Player1326State:
        return self.values[name]
