from euler_util import divisors

def euler21(upper_bound=10000):
    """http://projecteuler.net/index.php?section=problems&id=21
    
    Evaluate the sum of all amicable pairs under 10000."""
    div_table = {}
    amicables = set()
    for i in xrange(1, upper_bound):
        if not div_table.has_key(i):
            div_table[i] = sum(divisors(i))
        if not div_table.has_key(div_table[i]):
            div_table[div_table[i]] = sum(divisors(div_table[i]))
        if div_table[div_table[i]] == i and div_table[i] != i:
            amicables.add(div_table[i])
            amicables.add(div_table[div_table[i]])
    return sum(amicables)

