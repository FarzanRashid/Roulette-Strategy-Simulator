from bet import Bet
from players.player1326.player1326_state import Player1326State
from players.player1326.player1326_one_win import Player1326OneWin


class Player1326NoWins(Player1326State):
    _player1326_no_wins = None

    def __init__(self) -> None:
        super().__init__()
        self.betAmount = 1

    def __new__(cls, *args, **kwargs) -> "Player1326NoWins":
        if cls._player1326_no_wins is None:
            cls._player1326_no_wins = super().__new__(cls)
        return cls._player1326_no_wins

    def currentBet(self) -> Bet:
        return Bet(self.betAmount, self.outcome)

    def nextWon(self) -> Player1326State:
        return Player1326OneWin()
