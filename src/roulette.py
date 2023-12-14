from dataclasses import dataclass


# class Outcome:
#     def __init__(self, name: str, odds: int):
#         self.name = name
#         self.odds = odds
#
#     def winAmount(self, amount: float) -> float:
#         return self.odds * amount
#
#     def __eq__(self, other) -> bool:
#         return self.name == other.name
#
#     def __ne__(self, other) -> bool:
#         return self.name != other.name
#
#     def __hash__(self) -> int:
#         return hash(self.name)
#
#     def __str__(self) -> str:
#         return f"{self.name:s} ({self.odds:d}:1)"
#
#     def __repr__(self):
#         return f"{self.__class__.__name__:s}(name={self.name!r}, odds={self.odds!r})"

@dataclass(frozen=True)
class Outcome:
    """
    Outcome contains a single outcome on which a bet can be placed.
    There will be several hundred instances of Outcome objects on a given Roulette table.
    The minimum set of Outcome instances we will need are the 38 numbers, Red, and Black.
    The other instances will add details to our simulation.
    """

    name: str
    odds: int
