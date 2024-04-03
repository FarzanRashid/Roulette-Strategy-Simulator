import click
from wheel import Wheel
from bin_builder import BinBuilder
from table import Table
from game import Game
from simulator import Simulator
from strategy_factory import provide_strategy


@click.command()
@click.option('--strategy_name', prompt='Enter a strategy')
def main(strategy_name) -> None:  # pragma: no cover
    """
    A main application function that creates the necessary objects, runs the Simulator’s gather()
    method, and writes the available outputs to sys.stdout
    """
    wheel = Wheel()
    bin_builder = BinBuilder()
    table = Table()
    game = Game(wheel, table)
    bin_builder.buildBins(wheel)
    player = provide_strategy(strategy_name, table, wheel)
    simulator = Simulator(game, player)
    simulator.gather()

    print("maxima: ", simulator.maxima)
    print("Mean of maxima:", simulator.maxima.mean())
    print("Standard deviation of maxima:", simulator.maxima.stdev())

    print("duration: ", simulator.durations)
    print("Mean of duration:", simulator.durations.mean())
    print("Standard deviation of duration:", simulator.durations.stdev())


if __name__ == "__main__":  # pragma: no cover
    main()
