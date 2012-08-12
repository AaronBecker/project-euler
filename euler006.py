

def euler6(upper_bound=100):
    """http://projecteuler.net/problem=6

    The sum of the squares of the first ten natural numbers is
    1^2 + 2^2 + ... + 10^2 = 385
    The square of the sum of the first ten natural numbers is
    (1 + 2 + ... + 10)^2 = 55^2 = 3025
    Hence the difference between the sum of the squares of the first ten
    natural numbers and the square of the sum is 3025 - 385 = 2640.

    Find the difference between the sum of the squares of the first one hundred
    natural numbers and the square of the sum.
    """
    sum_sq = sum(x ** 2 for x in range(1, upper_bound + 1))
    sq_sum = sum(xrange(1, upper_bound + 1)) ** 2
    return sq_sum - sum_sq
