class Outcome:
    """
    :class:`Outcome` contains a single outcome on which a bet can be placed.

    In Roulette, each spin of the wheel has a number of :class:`Outcome` objects with bets that will be paid off.
    For example, the “1” bin has the following winning :class:`Outcome` instances: “1”, “Red”, “Odd”, “Low”,
    “Column 1”, “Dozen 1-12”,“Split 1-2”, “Split 1-4”, “Street 1-2-3”, “Corner 1-2-4-5”, “Five Bet”,
    “Line 1-2-3-4-5-6”, “00-0-1-2-3”, “Dozen 1”, “Low” and “Column 1”.

    All of thee above-named bets will pay off if the wheel spins a “1”. This makes a Wheel and a Bin fairly
    complex containers of :class:`Outcome` objects.

    ..  attribute:: name

        Holds the name of the :class:`Outcome`. Examples include "1", "Red".

    .. attribute:: odds

        Holds the payout odds for this :class:`Outcome`. Most odds are stated as 1:1 or 17:1, we only keep the numerator (17)
        and assume the denominator is 1.
    """

    def __init__(self, name: str, odds: int) -> None:
        """
        :param name: The name of this outcome
        :type name: str
        :param odds: The payout odds of this outcome.
        :type odds: int

        Sets the instance name and odds from the parameter name and odds.
        """
        self.name = name
        self.odds = odds

    def winAmount(self, amount: float) -> float:
        """
        Multiply this :class:`Outcome`’s odds by the given amount. The product is returned.

        :param amount: amount being bet
        :type amount: float
        """
        return self.odds * amount

    def __eq__(self, other) -> bool:
        """
        Compare the **name** attributes of **self** and **other**.

        :param other: Another :class:`Outcome` to compare against.
        :type other: :class:`Outcome`
        :return: True if this name matches the other name.
        :rtype: bool
        """
        return self.name == other.name

    def __ne__(self, other) -> bool:
        """
        Compare the **name** attributes of **self** and **other**.

        :param other: Another :class:`Outcome` to compare against.
        :type other: :class:`Outcome`
        :returns: True if this name does not match the other name.
        :rtype: bool
        """
        return self.name != other.name

    def __hash__(self) -> int:
        """
        Hash value for this outcome.

        :return: The hash value of the name, **hash(self.name)**.
        :rtype: int

        A hash calculation must include all of the attributes of an object that are essential to it’s distinct
        identity.In this case, we can return hash(self.name) because the odds aren’t really part of what makes
        an outcome distinct. Each outcome is an abstraction and a string name is all that identifies them.

        The definition for :func:`__hash__` in section 3.3.1 of the Language Reference Manual tells us to do the
        calculation using a modulus based on sys.hash_info.width. That value is the number of bits, the actual value
        we want to use is sys.hash_info.modulus, which is based on the width.
        """
        return hash(self.name)

    def __str__(self) -> str:
        """
        Easy-to-read representation of this outcome.

        This easy-to-read String output method is essential. This should return a **String**
        representation of the name and the odds. A form that looks like 1-2 Split (17:1) works
        nicely.

        :returns: String of the form *name (odds*:1).
        :rtype: str
        """
        return f"{self.name:s} ({self.odds:d}:1)"

    def __repr__(self):
        """
        Detailed representation of this outcome.

        :return: String of the form Outcome(name= *name*, odds= *odds*).
        :rtype: str
        """
        return f"{self.__class__.__name__:s}(name={self.name!r}, odds={self.odds!r})"
