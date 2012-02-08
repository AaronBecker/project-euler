from euler_util import LCM

def euler5(upper_bound=20):
    """http://projecteuler.net/problem=5

    2520 is the smallest number that can be divided by each of the numbers from
    1 to 10 without any remainder.

    What is the smallest positive number that is evenly divisible by all of the
    numbers from 1 to 20?
    """
    return LCM(range(1, upper_bound + 1))

