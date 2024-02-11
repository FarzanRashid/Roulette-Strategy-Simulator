import random
from typing import Dict, Iterator
from dataclasses import dataclass
from abc import ABC, abstractmethod


class InvalidBet(Exception):
    """
    :class:`InvalidBet` is raised when a Player instance attempts to place a bet which exceeds the
    table’s limit.

    This class simply inherits all features of its superclass.
    """


class Table:
    """
    :class:`Table` contains all the :class:`Bet` instances created by a :class:`Player` object. A
    table also has a betting limit, and the sum of all of a player’s bets must be less than or
    equal to this limit. We assume a single :class:`Player` object in the simulation.

    .. attribute:: limit

       This is the table limit. The sum of the bets from a :class:`Player` object must be less than
       or equal to this limit.

    .. attribute:: minimum

       This is the table minimum. Each individual bet from a :class:`Player` object must be greater
       than this limit.

    .. attribute:: bets

       This is a **list** of the :class:`Bet` instances currently active. These will result in
       either wins or losses to the :class:`Player` object.

    """

    def __init__(self, *bets) -> None:
        """
        Creates an empty **list** of bets.

        :param bets: A sequence of :class:`Bet` instances to initialize the table. If omitted,
                    an empty **list** will be used.
        """

        self.bets = list(bets) if bets else []
        self.minimum = 1
        self.limit = 300

    def placeBet(self, bet: Bet) -> None:
        """
        Adds the :class:`Bet` instance to the list of current bets.

        :param bet: A :class:`Bet` instance to be added to the table.
        """

        self.bets.append(bet)

    def __iter__(self) -> Iterator[Bet]:
        """
        Returns an iterator over the available list of :class:`Bet` instances. This simply returns
        the iterator over the list of :class:`Bet` objects.

        :return: iterator over all bets.
        """

        return iter(self.bets)

    def isValid(self) -> None:
        """
        **Raises:** :class:`InvalidBet` if the bets don’t pass the table limit rules.

        Applies the table-limit rules:

            - The sum of all bets is less than or equal to the table limit.

            - All bet amounts are greater than or equal to the table minimum.

        If there’s a problem an :class:`InvalidBet` exception is raised.
        """

        bets_sum = 0
        for bet in self.bets:
            bets_sum += bet.amount
            if bet.amount < self.minimum or bets_sum > self.limit:
                raise InvalidBet

    def __str__(self) -> str:
        """
        Returns an easy-to-read string representation of all current bets.

        :return: str
        """

        bet_strings = [str(bet) for bet in self.bets]
        if not bet_strings:
            return "No current bets"
        return "Current bets: \n:" + "\n".join(bet_strings)

    def __repr__(self) -> str:
        """
        Returns a representation of the form  :samp:`Table(bet, bet, ...)`.

        :return: str
        """

        bet_reprs = ", ".join(repr(bet) for bet in self.bets)
        return f"Table({bet_reprs})"


class Player(ABC):
    """
    :class:`Player` places bets in Roulette. This an abstract class, with no actual body for the
    **Player.placeBets()** method. However, this class does implement the basic **Player.win(
    )** method used by all subclasses.

    .. attribute::  stake

       The player’s current stake. Initialized to the player’s starting budget.

    .. attribute:: roundsToGo

       The number of rounds left to play. Initialized by the overall simulation control to the
       maximum number of rounds to play. In Roulette, this is spins. In Craps, this is the number of
       throws of the dice, which may be a large number of quick games or a small number of
       long-running games. In Craps, this is the number of cards played, which may be large
       number of hands or small number of multi-card hands.

    .. attribute:: table

       The :class:`Table` object used to place individual :class:`Bet` instances. The :class:`Table`
       object contains the current :class:`Wheel` object from which the player can get
       :class:`Outcome` objects used to build :class:`Bet` instances.
    """

    def __init__(self, table: Table) -> None:
        """
        Constructs the :class:`Player` instance with a specific :class:`Table` object for placing
        :class:`Bet` instances.

        :param table:  the table to use

        Since the table has access to the Wheel instance, we can use this wheel to extract
        :class:`Outcome` objects.
        """

        self.table = table
        self.stake = 100
        self.roundsToGo = 250

    def win(self, bet: Bet) -> None:
        """
        :param bet: The bet which won

        Notification from the :class:`Game` object that the :class:`Bet` instance was a winner. The
        amount of money won is available via the **Bet.winAmount()** method.
        """

        self.stake += bet.winAmount()

    def lose(self, bet: Bet) -> None:
        """
        :param bet: The bet which won

        Notification from the :class:`Game` object that the :class:`Bet` instance was a loser. Note
        that the amount was already deducted from the stake when the bet was created.
        """

    @abstractmethod
    def placeBets(self) -> None:
        """
        Updates the :class:`Table` object with the various :class:`Bet` objects.

        When designing the :class:`Table` class, we decided that we needed to deduct the amount of a
        bet from the stake when the bet is created. See the Table **Roulette Table Analysis**
        for more information.
        """

    def playing(self) -> bool:
        """
        Returns :samp:`True` while the player is still active.
        """
        return self.stake >= self.table.minimum and self.roundsToGo > 0


class Martingale(Player):
    """
    :class:`Martingale` is a :class:`Player` who places bets in Roulette. This player doubles their
    bet on every loss and resets their bet to a base amount on each win.

    .. attribute:: losscount

       The number of losses. This is the number of times to double the bet.

    .. attribute:: betMultiple

       The the bet multiplier, based on the number of losses. This starts at 1, and is reset to 1 on
       each win. It is doubled in each loss. This is always equal to :math:`2^{lossCount}`.
    """

    def __init__(self, table: Table):
        """
        Constructs the :class:`Martingale` :class:`Player` instance with a specific :class:`Table`
        object for placing :class:`Bet` instances.

        :param table: the table to use
        """

        super().__init__(table)
        self.losscount = 0
        self.betMultiple = 1

    def placeBets(self) -> None:
        """
        Updates the :class:`Table` object with a bet on “black”. The amount bet is
        :math:`2^{lossCount}`, which is the value of **betMultiple**.
        """

        outcome = Outcome("Black", 1)
        bet = Bet(self.betMultiple, outcome)
        self.table.placeBet(bet)
        try:
            self.table.isValid()
        except InvalidBet as exc:
            self.losscount = 0
            self.betMultiple = 2**self.losscount
            raise InvalidBet from exc
        self.stake -= self.betMultiple

    def playing(self) -> bool:
        if not super().playing() or self.betMultiple > self.stake:
            self.losscount = 0
            self.betMultiple = 2**self.losscount
            return False
        return True

    def win(self, bet: Bet) -> None:
        """
        :param bet: The bet which won

        Notification from the :class:`Game` object that the :class:`Bet` instance was a winner. The
        amount of money won is available via the **Bet.winAmount()** method.
        """

        super().win(bet)
        self.losscount = 0
        self.betMultiple = 2**self.losscount

    def lose(self, bet: Bet):
        """
        :param bet:

        Uses the superclass **Player.loss()** to do whatever bookkeeping the superclass already
        does.
        Increments **lossCount** by :samp:`1` and doubles **betMultiple**.
        """

        super().lose(bet)
        self.losscount += 1
        self.betMultiple = 2**self.losscount


class Passenger57(Player):
    """
    :class:`Passenger57` constructs a :class:`Bet` instance based on the :class:`Outcome` object
    named :samp:`"Black"`. This is a very persistent player.

    .. attribute:: black

       This is the outcome on which this player focuses their betting.

       This :class:`Player` will get this from the :class:`Wheel` using a well-known bet name.

    .. attribute:: table

       The :class:`Table` that is used to place individual :class:`Bet` instances.

    """

    def __init__(self, table: Table, wheel: Wheel) -> None:
        """
        Constructs the :class:`Player` instance with a specific table for placing bets. This also
        creates the “black” :class:`Outcome`. This is saved in a variable named
        **Passenger57.black** for use in creating bets.

        :param table: The :class:`Table` instance on which bets are placed.
        :param wheel: The :class:`Wheel` instance which defines all :class:`Outcome` instances.
        """

        super().__init__(table)
        self.table = table
        self.wheel = wheel
        self.black = self.wheel.getOutcome("Black")

    def placeBets(self) -> None:
        """
        Updates the :class:`Table` object with the various bets. This version creates a :class:`Bet`
        instance from the “Black” :class:`Outcome` instance. It uses **Table.placeBet()** to
        place that bet.

        """

        bet_amount = 20
        bet = Bet(bet_amount, self.black)
        self.table.placeBet(bet)
        self.stake -= bet_amount


class Game:
    """
    :class:`Game` manages the sequence of actions that defines the game of Roulette. This includes
    notifying the :class:`Player` object to place bets, spinning the :class:`Wheel` object and
    resolving the :class:`Bet` instances actually present on the :class:`Table` object.

    .. attribute:: wheel

       The :class:`Wheel` instance that returns a randomly selected :class:`Bin` object of
       :class:`Outcome` instances.

    .. attribute:: table

       The :class:`Table` object which contains the :class:`Bet` instances placed by the
       :class:`Player` object.

    .. attribute:: player

       The :class:`Player` object which creates :class:`Bet` instances at the :class:`Table` object.

    """

    def __init__(self, wheel: Wheel, table: Table) -> None:
        """
        Constructs a new :class:`Game`, using a given :class:`Wheel` and :class:`Table`.

        :param wheel: The :class:`Wheel` instance which produces random events
        :param table: The :class:`Table` instance which holds bets to be resolved.
        """

        self.wheel = wheel
        self.table = table

    def cycle(self, player: Player) -> None:
        """
        :param player: the individual player that places bets, receives winnings and pays losses.

        This will execute a single cycle of play with a given :class:`Player`. It will execute the
        following steps:

        1. Call **Player.placeBets()** method to create bets.
        2. Call **Wheel.choose()** method to get the next winning :class:`Bin` object.
        3. Call **iter()** on the :class:`table` to get all of the :class:`Bet` instances.
           For each :class:`Bet` instance, if the winning :class:`Bin` contains the
           :class:`Outcome`, call **Player.win()** method, otherwise, call the
           **Player.lose()** method.
        """

        player.placeBets()
        winning_bin = self.wheel.choose()
        for bet in self.table:
            if bet.outcome in winning_bin:
                player.win(bet)
            else:
                player.lose(bet)


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
        self.durations: list[int] = []
        self.maxima: list[int] = []

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
