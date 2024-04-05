import click
from wheel import Wheel
from bin_builder import BinBuilder
from table import Table
from game import Game
from simulator import Simulator
from player_factory import player_factory


@click.command()
@click.option("--player_name", prompt="Enter a player")
def main(player_name) -> None:  # pragma: no cover
    """
    A main application function that creates the necessary objects, runs the Simulator’s gather()
    method, and writes the available outputs to sys.stdout
    """
    wheel = Wheel()
    bin_builder = BinBuilder()
    table = Table()
    game = Game(wheel, table)
    bin_builder.buildBins(wheel)
    player = player_factory(player_name.capitalize(), table, wheel)
    simulator = Simulator(game, player)
    simulator.gather()

    print(f" \nSimulating {player_name} strategy \n")
    print("maxima: ", simulator.maxima)
    print("Mean of maxima:", simulator.maxima.mean())
    print("Standard deviation of maxima:", simulator.maxima.stdev(), "\n")

    print("duration: ", simulator.durations)
    print("Mean of duration:", simulator.durations.mean())
    print("Standard deviation of duration:", simulator.durations.stdev())


if __name__ == "__main__":  # pragma: no cover
    main()
