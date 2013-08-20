
import itertools
from collections import Counter

def euler62():
    """http://projecteuler.net/problem=62

    The cube, 41063625 (3453), can be permuted to produce two other cubes:
    56623104 (3843) and 66430125 (4053). In fact, 41063625 is the smallest cube
    which has exactly three permutations of its digits which are also cube.

    Find the smallest cube for which exactly five permutations of its digits
    are cube.
    """
    sorted_cubes = Counter()
    for i in itertools.count():
        # Note: reverse sorting ensures that we don't lose leading 0's.
        sc = int(''.join(sorted(str(i ** 3), reverse=True)))
        sorted_cubes[sc] += 1
        if sorted_cubes[sc] == 5:
            target = sc
            break
    for i in itertools.count():
        if target == int(''.join(sorted(str(i ** 3), reverse=True))):
            return i ** 3

