class Player1326State:
    def __init__(self, player: Player) -> None:
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
    def __init__(self, player: Player) -> None:
        self.values = {"Player1326NoWins": Player1326NoWins(player),
                       "Player1326OneWin": Player1326OneWin(player),
                       "Player1326TwoWins": Player1326TwoWins(player),
                       "Player1326ThreeWins": Player1326ThreeWins(player),
                       }

    def get(self, name: str) -> Player1326State:
        return self.values[name]
