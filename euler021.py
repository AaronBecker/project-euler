from euler_util import divisors


def euler21(upper_bound=10000):
    """http://projecteuler.net/problem=21

    Let d(n) be defined as the sum of proper divisors of n (numbers less than n
    which divide evenly into n).  If d(a) = b and d(b) = a, where a  b, then a
    and b are an amicable pair and each of a and b are called amicable numbers.

    For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44,
    55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4,
    71 and 142; so d(284) = 220.

    Evaluate the sum of all the amicable numbers under 10000.
    """
    div_table = {}
    amicables = set()
    for i in xrange(1, upper_bound):
        if not i in div_table:
            div_table[i] = sum(divisors(i))
        if not div_table[i] in div_table:
            div_table[div_table[i]] = sum(divisors(div_table[i]))
        if div_table[div_table[i]] == i and div_table[i] != i:
            amicables.add(div_table[i])
            amicables.add(div_table[div_table[i]])
    return sum(amicables)
