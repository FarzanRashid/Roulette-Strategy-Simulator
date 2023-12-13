class Outcome:
    def __init__(self, name: str, odds: int):
        self.name = name
        self.odds = odds

    def winAmount(self, amount: float) -> float:
        return self.odds * amount

    def __eq__(self, other) -> bool:
        return self.name == other.name
