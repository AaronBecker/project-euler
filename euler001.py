
def euler1(upper_bound=1000):
    """http://projecteuler.net/problem=1
    
    If we list all the natural numbers below 10 that are multiples of 3 or 5,
    we get 3, 5, 6 and 9. The sum of these multiples is 23.

    Find the sum of all the multiples of 3 or 5 below 1000.
    """
    fives = set(range(0, upper_bound, 5))
    threes = set(range(0, upper_bound, 3))
    return sum(fives | threes)

