from game import Game
from invalid_bet import InvalidBet
from integer_statistics import IntegerStatistics
from players.player import Player


class Simulator:
    """
    :class:`Simulator` exercises the Roulette simulation with a given :class:`Player` placing bets.
    It reports raw statistics on a number of sessions of play.

    .. attribute:: initDuration

       The duration value to use when initializing a :class:`Player` instance for a session. A
       default value of 250 is a good choice here.

    .. attribute:: initStake

       The stake value to use when initializing a :class:`Player` instance for a session. This is a
       count of the number of bets placed; i.e., 100 $10 bets is $1000 stake. A default value of 100
       is sensible.

    .. attribute:: samples

       The number of game cycles to simulate. A default value of 50 makes sense.

    .. attribute:: durations

       A **list** of lengths of time the :class:`Player` object remained in the game. Each session
       of play produces a duration metric, which are collected into this list.

    .. attribute:: maxima

       A **list** of maximum stakes for the :class:`Player` object. Each session of play produces a
       maximum stake metric, which are collected into this list.

    .. attribute:: player

       The :class:`Player` instance; essentially, the betting strategy we are simulating.

    .. attribute:: game

       The casino game we are simulating. This is an instance of the :class:`Game` class,
       which embodies the various rules, the :class:`Table` object and the :class:`Wheel` instance.
    """

    def __init__(self, game: Game, player: Player) -> None:
        """
        Saves the Player and :class:`Game` instances so we can gather statistics on the performance
        of the player’s betting strategy.

        :param game: The game we’re simulating. This includes the :class:`Table` and :class:`Wheel`.
        :param player: The player. This encapsulates the betting strategy.
        """

        self.game = game
        self.player = player
        self.initDuration = 250
        self.initStake = 100
        self.samples = 50
        self.durations = IntegerStatistics()
        self.maxima = IntegerStatistics()

    def session(self) -> list[int]:
        """
        :return: list of stake values.
        :rtype: list

        Executes a single game session. The :class:`Player` instance is initialized with their
        initial stake and initial cycles to go. An empty **list** of stake values is created.
        The session loop executes until the **Player.playing()** method returns false. This loop
        executes the **Game.cycle()** method; then it gets the stake from the :class:`Player` and
        appends this amount to the **list** of stake values. The **list** of individual stake
        values is returned as the result of the session of play.
        """

        self.player.stake = self.initStake
        self.player.roundsToGo = self.initDuration
        stake_values = []
        self.player.table.bets = []
        try:
            while self.player.playing():
                self.game.cycle(self.player)
                stake_values.append(self.player.stake)
                self.player.roundsToGo -= 1
        except InvalidBet:
            pass
        return stake_values

    def gather(self) -> None:
        """
        Executes the number of games sessions in samples. Each game session returns a **list** of
        stake values. When the session is over (either the play reached their time limit or their
        stake was spent), then the length of the session **list** and the maximum value in the
        session **list** are the resulting duration and maximum metrics. These two metrics are
        appended to the **durations** list and the **maxima** list.

        A client class will either display the durations and maxima raw metrics or produce
        statistical summaries.
        """

        for _ in range(self.samples):
            stake_values: list[int] = self.session()
            self.maxima.append(max(stake_values))
            self.durations.append(len(stake_values))
