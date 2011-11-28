# encoding: utf8
from euler_util import expmod


def hyperexpmod(base, exp, mod):
    result = 1
    while exp > 0:
        result, exp = expmod(base, result, mod), exp - 1
    return result


def euler188():
    """http://projecteuler.net/problem=188
    
    The hyperexponentiation or tetration of a number a by a positive integer
    b, denoted by a↑↑b or ba, is recursively defined by:

    a↑↑1 = a,
    a↑↑(k+1) = a(a↑↑k).

    Thus we have e.g. 3↑↑2 = 33 = 27, hence 3↑↑3 = 327 = 7625597484987 and
    3↑↑4 is roughly 103.6383346400240996*10^12.

    Find the last 8 digits of 1777↑↑1855.
    """
    return hyperexpmod(1777, 1855, 10 ** 8)
