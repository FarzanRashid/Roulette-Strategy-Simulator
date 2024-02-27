from abc import abstractmethod
from bet import Bet
from player import Player


class Player1326State:
    def __init__(self, player: Player) -> None:
        self.player = player

    @abstractmethod
    def currentBet(self) -> Bet:
        return NotImplemented

    @abstractmethod
    def nextWon(self) -> "Player1326State":
        return NotImplemented

    def nextLost(self) -> "Player1326State":
        pass


class Player1326NoWin(Player1326State):
    _player1326_nowin = None

    def __init__(self, player: Player) -> None:
        super().__init__(player)

    def __new__(cls, *args, **kwargs) -> "Player1326NoWin":
        if cls._player1326_nowin is None:
            cls._player1326_nowin = super(Player1326NoWin, cls).__new__(cls)
        return cls._player1326_nowin

    def currentBet(self) -> Bet:
        bet_amount = 1
        return Bet(bet_amount, self.player.outcome)

    def nextWon(self) -> Player1326State:
        return Player1326OneWin(self.player)


class Player1326OneWin(Player1326State):
    _player1326_onewin = None

    def __init__(self, player: Player) -> None:
        super().__init__(player)

    def __new__(cls, *args, **kwargs) -> "Player1326OneWin":
        if cls._player1326_onewin is None:
            cls._player1326_onewin = super(Player1326OneWin, cls).__new__(cls)
        return cls._player1326_onewin

    def currentBet(self) -> Bet:
        bet_amount = 3
        return Bet(bet_amount, self.player.outcome)

    def nextWon(self) -> Player1326State:
        return Player1326TwoWins(self.player)


class Player1326TwoWins(Player1326State):
    _player1326_two_wins = None

    def __init__(self, player: Player) -> None:
        super().__init__(player)

    def __new__(cls, *args, **kwargs) -> "Player1326TwoWins":
        if cls._player1326_two_wins is None:
            cls._player1326_two_wins = super(Player1326TwoWins, cls).__new__(cls)
        return cls._player1326_two_wins

    def currentBet(self) -> Bet:
        bet_amount = 2
        return Bet(bet_amount, self.player.outcome)

    def nextWon(self) -> Player1326State:
        return Player1326ThreeWins(self.player)


class Player1326ThreeWins(Player1326State):
    _player1326_three_wins = None

    def __init__(self, player: Player) -> None:
        super().__init__(player)

    def __new__(cls, *args, **kwargs) -> "Player1326ThreeWins":
        if cls._player1326_three_wins is None:
            cls._player1326_three_wins = super(Player1326ThreeWins, cls).__new__(cls)
        return cls._player1326_three_wins

    def currentBet(self) -> Bet:
        bet_amount = 2
        return Bet(bet_amount, self.player.outcome)

    def nextWon(self) -> Player1326State:
        return Player1326NoWin(self.player)
