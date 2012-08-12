from euler_util import is_palindrome


def euler55():
    """http://projecteuler.net/problem=55

    2520 is the smallest number that can be divided by each of the numbers from
    1 to 10 without any remainder.

    What is the smallest positive number that is evenly divisible by all of the
    numbers from 1 to 20?
    """
    lychrel = []
    for n in range(10000):
        candidate = n
        is_lychrel = True
        for round in range(50):
            candidate += int(str(candidate)[::-1])
            if is_palindrome(candidate):
                is_lychrel = False
                break
        if is_lychrel:
            lychrel.append(n)
    return len(lychrel)
