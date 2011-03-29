
from itertools import permutations

def is_divisible(s):
    return int(s[7:10]) % 17 == 0 and \
            int(s[6:9]) % 13 == 0 and \
            int(s[5:8]) % 11 == 0 and \
            int(s[4:7]) % 7 == 0 and \
            int(s[3:6]) % 5 == 0 and \
            int(s[2:5]) % 3 == 0 and \
            int(s[1:4]) % 2 == 0

def euler43():
    """http://projecteuler.net/index.php?section=problems&id=43
    
    Find the sum of all pandigital numbers with an unusual substring
    divisibility property."""
    return sum(int(''.join(t)) for t in permutations('1234567890') \
            if is_divisible(''.join(t)))

