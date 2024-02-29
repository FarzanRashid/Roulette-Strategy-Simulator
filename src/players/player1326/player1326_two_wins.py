from bet import Bet
from players.player1326.player1326_state import Player1326State
from players.player1326.player1326_three_wins import Player1326ThreeWins


class Player1326TwoWins(Player1326State):
    _player1326_two_wins = None

    def __init__(self) -> None:
        super().__init__()
        self.betAmount = 2

    def __new__(cls, *args, **kwargs) -> "Player1326TwoWins":
        if cls._player1326_two_wins is None:
            cls._player1326_two_wins = super().__new__(cls)
        return cls._player1326_two_wins

    def currentBet(self) -> Bet:
        return Bet(self.betAmount, self.outcome)

    def nextWon(self) -> Player1326State:
        return Player1326ThreeWins(self.player)
