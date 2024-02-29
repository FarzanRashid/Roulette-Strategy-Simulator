from bet import Bet
from players.player1326.player1326_state import Player1326State
from players.player1326.player1326_two_wins import Player1326TwoWins


class Player1326OneWin(Player1326State):
    _player1326_onewin = None

    def __init__(self) -> None:
        super().__init__()
        self.betAmount = 3

    def __new__(cls, *args, **kwargs) -> "Player1326OneWin":
        if cls._player1326_onewin is None:
            cls._player1326_onewin = super().__new__(cls)
        return cls._player1326_onewin

    def currentBet(self) -> Bet:
        return Bet(self.betAmount, self.player.outcome)

    def nextWon(self) -> Player1326State:
        return Player1326TwoWins(self.player)
