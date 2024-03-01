from bet import Bet
from players.player1326.player1326_state import Player1326State


class Player1326ThreeWins(Player1326State):
    _player1326_three_wins = None

    def __init__(self) -> None:
        super().__init__()
        self.betAmount = 6

    def __new__(cls, *args, **kwargs) -> "Player1326ThreeWins":
        if cls._player1326_three_wins is None:
            cls._player1326_three_wins = super().__new__(cls)
        return cls._player1326_three_wins

    def currentBet(self) -> Bet:
        return Bet(self.betAmount, self.outcome)

    def nextWon(self) -> Player1326State:
        return super().nextLost()
