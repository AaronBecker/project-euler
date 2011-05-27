
import itertools

def euler62():
    """http://projecteuler.net/index.php?section=problems&id=62
    
    The cube, 41063625 (3453), can be permuted to produce two other cubes:
    56623104 (3843) and 66430125 (4053). In fact, 41063625 is the smallest cube
    which has exactly three permutations of its digits which are also cube.

    Find the smallest cube for which exactly five permutations of its digits
    are cube.
    """
    sorted_cubes = {}
    for i in itertools.count():
        sc = int(''.join(sorted(str(i**3), reverse=True)))
        if sc in sorted_cubes: sorted_cubes[sc] += 1
        else: sorted_cubes[sc] = 1
        if sorted_cubes[sc] == 5:
            target = sc
            break
    for i in itertools.count():
        if target == int(''.join(sorted(str(i**3), reverse=True))):
            return i**3
        
