import random
from typing import Dict, Iterator
from dataclasses import dataclass
from abc import ABC, abstractmethod


def main() -> None:  # pragma: no cover
    """
    A main application function that creates the necessary objects, runs the Simulator’s gather()
    method, and writes the available outputs to sys.stdout
    """
    wheel = Wheel()
    bin_builder = BinBuilder()
    table = Table()
    game = Game(wheel, table)
    martingale = Martingale(table)
    simulator = Simulator(game, martingale)

    bin_builder.buildBins(wheel)
    simulator.gather()

    print("maxima: ", simulator.maxima)
    print("duration: ", simulator.durations)


if __name__ == "__main__":
    main()  # pragma: no cover
