
def is_power_sum(number):
    return number == sum([int(c) ** 5 for c in str(number)])

def euler30():
    """http://projecteuler.net/index.php?section=problems&id=30

    Find the sum of all the numbers that can be written as the sum of fifth
    powers of their digits."""
    # note: 9**5 = 59049, so no number over 6 * 9**5 = 354294 qualifies
    return sum(filter(is_power_sum, range(2, 354295)))

