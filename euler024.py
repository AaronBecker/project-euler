from euler_util import permutations

def euler24():
    """http://projecteuler.net/index.php?section=problems&id=24
    
    What is the millionth lexicographic permutation of the digits
    0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?"""
    return sorted(list(permutations("0123456789")))[10**6 - 1]

