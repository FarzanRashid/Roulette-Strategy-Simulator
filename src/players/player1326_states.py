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
    def __init__(self, player: Player) -> None:
        super().__init__(player)

    def currentBet(self) -> Bet:
        bet_amount = 1
        return Bet(bet_amount, self.player.outcome)

    def nextWon(self) -> Player1326State:
        pass


class Player1326OneWin(Player1326State):
    def __init__(self, player: Player) -> None:
        super().__init__(player)

    def currentBet(self) -> Bet:
        bet_amount = 3
        return Bet(bet_amount, self.player.outcome)

    def nextWon(self) -> Player1326State:
        pass


class Player1326TwoWins(Player1326State):
    def __init__(self, player: Player) -> None:
        super().__init__(player)

    def currentBet(self) -> Bet:
        bet_amount = 2
        return Bet(bet_amount, self.player.outcome)

    def nextWon(self) -> Player1326State:
        pass


class Player1326ThreeWins(Player1326State):
    def __init__(self, player: Player) -> None:
        super().__init__(player)

    def currentBet(self) -> Bet:
        bet_amount = 2
        return Bet(bet_amount, self.player.outcome)

    def nextWon(self) -> Player1326State:
        return Player1326NoWin(self.player)
