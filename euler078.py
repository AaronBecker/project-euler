
import itertools

def euler78():
    """http://projecteuler.net/problem=78

    Let p(n) represent the number of different ways in which n coins can be
    separated into piles. For example, five coins can separated into piles in
    exactly seven different ways, so p(5)=7.

    OOOOO
    OOOO   O
    OOO   OO
    OOO   O   O
    OO   OO   O
    OO   O   O   O
    O   O   O   O   O

    Find the least value of n for which p(n) is divisible by one million.
    """
    # Same generating function approach as #76, but modulo 10**6.
    p = [1]
    for i in itertools.count(1):
        j, k, s = 1, 1, 0
        while j > 0:
            j = i - (3 * k * k + k) // 2
            if j >= 0:
                s -= (-1) ** k * p[j]
            j = i - (3 * k * k - k) // 2
            if j >= 0:
                s -= (-1) ** k * p[j]
            k += 1
        p.append(s % 10**6)
        if p[-1] == 0: return len(p) - 1
