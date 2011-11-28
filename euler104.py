
import itertools

digits = set('123456789')
def is_pandigital(s):
    return set(s) == digits

def euler104():
    """projecteuler.net/problem=104
    
    FIXME: add description.
    """
    n1, n2, tail1, tail2 = 0, 1, 0, 1
    for i in itertools.count():
        n1, n2 = n2, n1 + n2
        tail1, tail2 = tail2, (tail1 + tail2) % 10 ** 9
        if is_pandigital(str(tail1)) and is_pandigital(str(n1)[:9]):
            return i + 1


