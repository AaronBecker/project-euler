
from math import factorial


def euler15(n=20):
    """http://projecteuler.net/problem=15

    Starting in the top left corner of a 2x2 grid, there are 6 routes (without
    backtracking) to the bottom right corner.

    How many routes are there through a 2020 grid?
    """
    # simple combinatorics, 2n choose n
    return factorial(2 * n) / (factorial(n) ** 2)
