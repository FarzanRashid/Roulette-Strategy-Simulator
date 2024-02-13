class Bin(frozenset):
    """
    :class:`Bin` contains a collection of :class:`Outcome` instances which reflect the winning bets
    that are paid for a particular bin on a Roulette wheel. In Roulette, each spin of the wheel
    has a number of :class:`Outcome` instances. Example: A spin of 1, selects the “1” bin with
    the following winning :class:`Outcome` instances: “1” , “Red”, “Odd”,“Low” , “Column 1” ,
    “Dozen 1-12” , “Split 1-2” , “Split 1-4” , “Street 1-2-3” , “Corner 1-2-4-5”, “Five Bet”,
    “Line 1-2-3-4-5-6” , “00-0-1-2-3” , “Dozen 1”, “Low” and “Column 1”. These are collected into a
    single :class:`Bin`.
    """
