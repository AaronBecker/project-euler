
def is_power_sum(number):
    return number == sum([int(c) ** 5 for c in str(number)])

def euler30():
    """Find the sum of all the numbers that can be written as the
    sum of fifth powers of their digits."""
    # note: 9**5 = 59049, so no number over 6 * 9**5 = 354294 qualifies
    term_sum = sum(filter(is_power_sum, range(2, 354295)))
    print 'The sum of all numbers that are the sum of the fifth powers of '\
            'their digits is %d' % term_sum
    return term_sum
