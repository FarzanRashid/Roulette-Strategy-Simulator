from abc import abstractmethod
from bet import Bet
from outcome import Outcome


class Player1326State:
    def __init__(self) -> None:
        self.betAmount: int = 0
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
        return Bet(self.betAmount, self.outcome)

    def nextWon(self) -> Player1326State:
        return Player1326TwoWins()


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
        return Player1326ThreeWins()
