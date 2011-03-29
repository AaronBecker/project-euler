from euler_util import factorial

digit_factorials = [ factorial(0), factorial(1), factorial(2),
        factorial(3), factorial(4), factorial(5), factorial(6),
        factorial(7), factorial(8), factorial(9)]

def factorial_sum(n):
    return n == sum([digit_factorials[int(c)] for c in str(n)])

def euler34():
    """http://projecteuler.net/index.php?section=problems&id=34
    
    Find the sum of all numbers which are equal to the sum of the factorial of
    their digits."""
    # note: 7 * 9! = 2540160 < 10 ** 7, so we don't need to look any higher
    return sum(filter(factorial_sum, range(10, 2540161)))

