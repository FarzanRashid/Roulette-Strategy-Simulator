class Card:
    """
    Superclass for cards.
    >>> c2d = Card(2, Card.Diamonds)
    >>> c2d.softValue
    2
    >>> c2d.hardValue
    2
    """

    Clubs = u"\N{BLACK CLUB SUIT}"
    Diamonds = u"\N{WHITE DIAMOND SUIT}"
    Hearts = u"\N{WHITE HEART SUIT}"
    Spades = u"\N{BLACK SPADE SUIT}"
    Jack = 11
    Queen = 12
    King = 13
    Ace = 1

    def __init__(self, rank: int, suit: str) -> None:
        assert suit in (Card.Clubs, Card.Diamonds, Card.Hearts, Card.Spades)
        assert 1 <= rank < 14
        self.rank = rank
        self.suit = suit
        self.order = rank

    @property
    def hardValue(self) -> int:
        return self.rank

    @property
    def softValue(self) -> int:
        return self.rank


class AceCard(Card):
    """
    >>> cas = AceCard(Card.Ace, Card.Spades)
    >>> str(cas)
    ' A♠'
    >>> cas.softValue
    11
    """

    def __init__(self, rank, suit):
        assert rank == 1
        super().__init__(rank, suit)
        self.rank = rank
        self.order = 14

    def __str__(self):
        return f" A{self.suit}"

    @property
    def hardValue(self) -> int:
        return 1

    @property
    def softValue(self) -> int:
        return 11
