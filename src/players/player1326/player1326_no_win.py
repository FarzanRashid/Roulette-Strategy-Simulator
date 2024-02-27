
class Player1326NoWins(Player1326State):
    _player1326_no_wins = None

    def __init__(self, player: Player) -> None:
        super().__init__(player)
        self.betAmount = 1

    def __new__(cls, *args, **kwargs) -> "Player1326NoWins":
        if cls._player1326_no_wins is None:
            cls._player1326_no_wins = super().__new__(cls)
        return cls._player1326_no_wins

    def currentBet(self) -> Bet:
        return Bet(self.betAmount, self.player.outcome)

    def nextWon(self) -> Player1326State:
        return Player1326OneWin(self.player)
