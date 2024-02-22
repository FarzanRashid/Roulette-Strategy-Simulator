import random
from typing import Dict, Iterator
from outcome import Outcome
from bin import Bin


class Wheel:
    """
    :class:`Wheel` contains the 38 individual bins on a Roulette wheel, plus a random number
    generator. It can select a :class:`Bin` at random, simulating a spin of the Roulette wheel.

    .. attribute:: bins

        Contains the individual Bin instances.

        This is a tuple of 38 elements. This can be built with ``tuple(Bin() for i in
        range(38))``

    .. attribute:: rng

        A random number generator to select a :class:`Bin` from the **bins** collection.

        For testing, we’ll often want to seed this generator. For simulation processing, we can
        set the seed value using ``os.urandom()``.
    """

    def __init__(self) -> None:
        """
        Creates a new wheel with 38 empty Bin instances. It will also create a new random number
        generator instance.

        At the present time, this does not do the full initialization of the Bin instances. We’ll
        rework this in a future exercise.
        """
        self.bins = tuple(Bin() for _ in range(38))
        self.rng = random.Random()
        self.all_outcomes: Dict[str, Outcome] = {}

    def addOutcome(self, number: int, outcome: Outcome) -> None:
        """
        Adds the given :class:`Outcome` object to the :class:`Bin` instance with the given number.

        :param number: bin number, in the range zero to 37 inclusive.
        :type number: int
        :param outcome: The Outcome to add to this Bin
        :type outcome: Outcome
        """
        updated_bin = Bin(list(self.bins[number].union(Bin([outcome]))))
        self.bins = self.bins[:number] + (updated_bin,) + self.bins[number + 1 :]

        self.all_outcomes[outcome.name] = outcome

    def choose(self) -> Bin:
        """
        Generates a random number between 0 and 37, and returns the randomly selected Bin instance.

        The **Random.choice()** function of the **random** module will select one of the available
        :class:`Bin` instances from the **bins** collection.

        :return: A Bin selected at random from the wheel.
        :rtype: Bin
        """
        return self.rng.choice(self.bins)

    def get(self, bin: int) -> Bin:
        """
        Returns the given Bin instance from the internal collection.

        :param bin: bin number, in the range zero to 37 inclusive.
        :type bin: int
        :return: The requested Bin.
        :rtype: Bin
        """
        return self.bins[bin]

    def getOutcome(self, name: str) -> Outcome:
        """
        Retrieve an :class:`Outcome` object based on the provided name.

        This method searches for an :class:`Outcome` with the specified name in the collection of
        all outcomes (`all_outcomes`). If the outcome is found, it is returned. Otherwise,
        a KeyError is raised with an error message.

        :param name: the name of an :class:`Outcome`
        :return: the :class:`Outcome` object
        :rtype: :class:`Outcome`
        """
        if name not in self.all_outcomes:
            raise KeyError(f"Outcome with {name} not found")
        return self.all_outcomes[name]

    def binIterator(self) -> Iterator[Bin]:
        """
        Returns an **Iterator** of :py:class:`~bin.Bin` objects.

        :return: **Iterator** of :py:class:`~bin.Bin` objects.
        :rtype: Iterator
        """

        return iter(self.bins)
