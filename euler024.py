from euler_util import permutations

def euler24():
    """What is the millionth lexicographic permutation of the digits
    0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?"""
    p = list(permutations("0123456789"))
    p.sort()
    print 'The millionth lexicographic permutation of 0-9 is %s'\
            % p[10 ** 6 - 1]
    return p[10 ** 6 - 1]
