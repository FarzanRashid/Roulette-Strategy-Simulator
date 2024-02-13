from dataclasses import dataclass
from outcome import Outcome


@dataclass
class Bet:
    """
    :class:`Bet` associates an amount and an :class:`Outcome`. In a future round of design, we can
    also associate a :class:`Bet` with a :class:`Player`.

    .. attribute:: amount

        The amount of the bet.

    .. attribute:: outcome

        The :class:`Outcome` on which the bet is placed.
    """

    amount: int
    outcome: Outcome

    def winAmount(self) -> int:
        """
        Uses the :class:`Outcome`’s **winAmount** to compute the amount won, given the amount of
        this bet. Note that the amount bet must also be added in. A 1:1 outcome (e.g. a bet on Red)
        pays the amount bet plus the amount won.

        :return:  amount won
        :rtype: int
        """
        return int(self.amount + self.outcome.winAmount(float(self.amount)))

    def loseAmount(self) -> int:
        """
        Returns the amount bet as the amount lost. This is the cost of placing the bet.


        :return: Returns the amount bet as the amount lost. This is the cost of placing the bet.
        :rtype: int
        """
        return self.amount

    def __str__(self) -> str:
        """
        Returns a string representation of this bet. Note that this method will delegate the much of
        the work to the **__str__()** method of the :class:`Outcome`.

        :return: string representation of this bet with the form  :samp:`"{amount} on {outcome}"`
        :rtype: str
        """
        return f"{self.amount} on {self.outcome}"
