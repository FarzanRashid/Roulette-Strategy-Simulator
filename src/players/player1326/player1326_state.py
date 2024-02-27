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