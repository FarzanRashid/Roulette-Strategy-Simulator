from table import Table
from wheel import Wheel
from players.player import Player
from players.martingale import Martingale
from players.cancellation import PlayerCancellation
from players.fibonacci import PlayerFibonacci
from players.seven_reds import SevenReds
from players.random import PlayerRandom
from players.passenger57 import Passenger57
from players.player1326.player1326 import Player1326


def provide_player(player_name: str, table: Table, wheel: Wheel) -> Player:
    """
    Returns an object of desired Player class.
    """

    players = {
        "Martingale": Martingale(table),
        "Cancellation": PlayerCancellation(table),
        "Fibonacci": PlayerFibonacci(table),
        "Sevenreds": SevenReds(table),
        "Random": PlayerRandom(table, wheel),
        "Passenger57": Passenger57(table, wheel),
        "Player1326": Player1326(table),
    }
    if player_name not in players:
        raise ValueError("Player not found, enter a valid player name")
    return players[player_name]
