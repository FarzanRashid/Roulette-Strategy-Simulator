class Outcome:
    def __init__(self, name: str, odds: int):
        self.name = name
        self.odds = odds

    def winAmount(self, amount: float) -> float:
        return self.odds * amount

    def __eq__(self, other) -> bool:
        return self.name == other.name

    def __ne__(self, other) -> bool:
        return self.name != other.name

    def __hash__(self) -> int:
        return hash(self.name)

    def __str__(self) -> str:
        return f"{self.name:s} ({self.odds:d}:1)"

    def __repr__(self):
        return f"{self.__class__.__name__:s}(name={self.name!r}, odds={self.odds!r})"
