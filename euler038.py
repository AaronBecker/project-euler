
from euler_util import is_pandigital

def forms_pandigital(n):
    concat = str(n)
    for i in itertools.count(2):
        concat += str(n*i)
        if len(concat) == 9 and is_pandigital(int(concat)): return int(concat)
        elif len(concat) > 9: return 0

def euler38():
    """What is the largest 1 to 9 pandigital that can be formed by multiplying
    a fixed number by 1, 2, 3, ... ?"""
    biggest = max(forms_pandigital(n) for n in xrange(100000))
    print 'The target pandigital is %d' % biggest
    return max

