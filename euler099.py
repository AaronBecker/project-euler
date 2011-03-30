
from math import log

def euler99():
    """http://projecteuler.net/index.php?section=problems&id=99
    
    Which base/exponent pair in the file has the greatest numerical value?"""
    pairs = map(lambda x:map(int, x.split(',')),
            open('euler099_input.txt').read().split())
    return max(zip(map(lambda x: x[1]*log(x[0]), pairs),
        xrange(1, len(pairs))))[1]
