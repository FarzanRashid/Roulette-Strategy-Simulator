from abc import abstractmethod
from bet import Bet
from players.player1326.player1326 import Player1326
from players.player1326.player1326_no_wins import Player1326NoWins
from players.player1326.player1326_one_win import Player1326OneWin
from players.player1326.player1326_two_wins import Player1326TwoWins
from players.player1326.player1326_three_wins import Player1326ThreeWins


class Player1326State:
    def __init__(self, player: Player1326) -> None:
        self.player = player
        self.betAmount = None

    @abstractmethod
    def currentBet(self) -> Bet:
        return NotImplemented

    @abstractmethod
    def nextWon(self) -> "Player1326State":
        return NotImplemented

    def nextLost(self) -> "Player1326NoWins":
        return Player1326NoWins(self.player)


class Player1326StateFactory:
    def __init__(self, player: Player1326) -> None:
        self.values = {"Player1326NoWins": Player1326NoWins(player),
                       "Player1326OneWin": Player1326OneWin(player),
                       "Player1326TwoWins": Player1326TwoWins(player),
                       "Player1326ThreeWins": Player1326ThreeWins(player),
                       }

    def get(self, name: str) -> Player1326State:
        return self.values[name]
