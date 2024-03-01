from abc import abstractmethod
from bet import Bet
from outcome import Outcome


class Player1326State:
    def __init__(self) -> None:
        self.betAmount = None
        self.outcome = Outcome("Red", 1)

    @abstractmethod
    def currentBet(self) -> Bet:
        return NotImplemented

    @abstractmethod
    def nextWon(self) -> "Player1326State":
        return NotImplemented

    def nextLost(self) -> "Player1326State":
        from players.player1326.player1326_no_wins import Player1326NoWins
        return Player1326NoWins()
