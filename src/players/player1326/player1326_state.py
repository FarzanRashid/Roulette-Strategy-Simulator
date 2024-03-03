from abc import abstractmethod
from bet import Bet
from outcome import Outcome


class Player1326State:
    """
    :class:`Player1326State` is the superclass for all of the states in the 1-3-2-6 betting system.
    """

    def __init__(self) -> None:
        """
        The constructor for this class saves the Player1326 instance.
        """

        self.betAmount: int = 0
        self.outcome = Outcome("Red", 1)

    @abstractmethod
    def currentBet(self) -> Bet:
        """
        Constructs a new :py:class:`~bet.Bet` object from the player’s preferred
        :py:class:`~outcome.Outcome` instance. Each subclass provides a different multiplier used
        when creating this :py:class:`~bet.Bet` object.

        In Python, the superclass method should return ``NotImplemented``. This is a big debugging aid,
        it helps us locate subclasses which did not provide a method body.
        """

        return NotImplemented

    @abstractmethod
    def nextWon(self) -> "Player1326State":
        """
        Constructs the new :class:`Player1326State` instance to be used when the bet was a winner.

        In Python, this method should return ``NotImplemented``. This is a big debugging aid, it
        helps us locate subclasses which did not provide a method body.

        Note the type hint for this method is provided as a string. We can’t reference the
        :class:`Player1326State` type within the body of the class definition. Instead of naming the
        type directly, we use a string.
        """

        return NotImplemented

    def nextLost(self) -> "Player1326NoWins":
        """
        Constructs the new :class:`Player1326State` instance to be used when the bet was a loser.
        This method is the same for each subclass: it creates a new instance of
        :class:`Player1326NoWins`.

        This defined in the superclass to assure that it is available for each subclass.
        """

        return Player1326NoWins()


class Player1326NoWins(Player1326State):
    """
    :class:`Player1326NoWins` defines the bet and state transition rules in the 1-3-2-6 betting
    system. When there are no wins, the base bet value of 1 is used.
    """

    _player1326_no_wins = None

    def __init__(self) -> None:
        super().__init__()
        self.betAmount = 1

    def __new__(cls, *args, **kwargs) -> "Player1326NoWins":
        if cls._player1326_no_wins is None:
            cls._player1326_no_wins = super().__new__(cls)
        return cls._player1326_no_wins

    def currentBet(self) -> Bet:
        """
        Constructs a new :py:class:`~bet.Bet` from the player’s :py:class:`~outcome.Outcome`
        information. The bet multiplier is 1.
        """

        return Bet(self.betAmount, self.outcome)

    def nextWon(self) -> Player1326State:
        """
        Constructs the new :class:`Player1326OneWin` instance to be used when the bet was a winner.
        """

        return Player1326OneWin()


class Player1326OneWin(Player1326State):
    """
    :class:`Player1326OneWin` defines the bet and state transition rules in the 1-3-2-6 betting
    system. When there is one wins, the base bet value of 3 is used.
    """

    _player1326_onewin = None

    def __init__(self) -> None:
        super().__init__()
        self.betAmount = 3

    def __new__(cls, *args, **kwargs) -> "Player1326OneWin":
        if cls._player1326_onewin is None:
            cls._player1326_onewin = super().__new__(cls)
        return cls._player1326_onewin

    def currentBet(self) -> Bet:
        """
        Constructs a new :py:class:`~bet.Bet` from the player’s :py:class:`~outcome.Outcome`
        information. The bet multiplier is 3.
        """

        return Bet(self.betAmount, self.outcome)

    def nextWon(self) -> Player1326State:
        """
        Constructs the new :class:`Player1326TwoWins` instance to be used when the bet was a winner.
        """

        return Player1326TwoWins()


class Player1326TwoWins(Player1326State):
    """
    :class:`Player1326TwoWins` defines the bet and state transition rules in the 1-3-2-6 betting
    system. When there are two wins, the base bet value of 2 is used.
    """

    _player1326_two_wins = None

    def __init__(self) -> None:
        super().__init__()
        self.betAmount = 2

    def __new__(cls, *args, **kwargs) -> "Player1326TwoWins":
        if cls._player1326_two_wins is None:
            cls._player1326_two_wins = super().__new__(cls)
        return cls._player1326_two_wins

    def currentBet(self) -> Bet:
        """
        Constructs a new :py:class:`~bet.Bet` from the player’s :py:class:`~outcome.Outcome`
        information. The bet multiplier is 2.
        """

        return Bet(self.betAmount, self.outcome)

    def nextWon(self) -> Player1326State:
        return Player1326ThreeWins()


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

    def nextWon(self) -> Player1326NoWins:
        return Player1326NoWins()
