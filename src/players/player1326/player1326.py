from bet import Bet
from table import Table
from players.player import Player
from players.player1326.player1326_state_factory import Player1326StateFactory


class Player1326(Player):
    """
    :class:`Player1326` follows the 1-3-2-6 betting system. The player has a preferred
    :py:class:`~outcome.Outcome` instance. This should be an even money bet like red, black,
    even, odd, high or low. The player also has a current betting state that determines the current
    bet to place, and what next state applies when the bet has won or lost.

    .. attribute:: state

       This is the current state of the 1-3-2-6 betting system. It will be an instance of a subclass
       of :py:class:`~players.player1326.player1326_state.Player1326State`  class. This will be
       one of the four states: No Wins, One Win, Two Wins or Three Wins.
    """

    def __init__(self, table: Table) -> None:
        """
        Initializes the state. The state is set to the initial state of an instance of
        ~players.player1326.player1326_state.Player1326NoWins` class.

        :param table: The :py:class:`~table.Table` object which will accept the bets.
        """

        super().__init__(table)
        self.table = table
        self.state = Player1326StateFactory().get("Player1326NoWins")

    def playing(self) -> bool:
        return super().playing() and self.stake >= self.state.betAmount

    def placeBets(self) -> None:
        """
        Updates the :py:class:`~table.Table` with a bet created by the current state.
        This method delegates the bet creation to state object’s **currentBet()** method.
        """

        self.table.placeBet(self.state.currentBet())
        self.stake -= self.state.betAmount

    def win(self, bet: Bet) -> None:
        super().win(bet)
        self.state = self.state.nextWon()

    def lose(self, bet: Bet) -> None:
        self.state = self.state.nextLost()
