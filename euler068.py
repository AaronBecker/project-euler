
import itertools

def magic_string(numbers):
    size = len(numbers) / 2
    inner, outer = numbers[size:], numbers[:size]
    if min(outer) != outer[0]: return False # ensure canonical form

    magic_number = outer[0] + inner[0] + inner[1]
    canonical_string = []
    for i in range(size):
        a, b, c = outer[i], inner[i], inner[(i + 1) % size]
        if sum((a, b, c)) != magic_number: return False
        canonical_string.extend((a, b, c))
    return canonical_string


def euler68():
    """http://projecteuler.net/index.php?section=problems&id=68

    Consider the following "magic" 3-gon ring, filled with the numbers 1 to 6,
    and each line adding to nine.

    Working clockwise, and starting from the group of three with the
    numerically lowest external node (4,3,2 in this example), each solution can
    be described uniquely. For example, the above solution can be described by
    the set: 4,3,2; 6,2,1; 5,1,3.

    It is possible to complete the ring with four different totals: 9, 10, 11,
    and 12. There are eight solutions in total.

    Total	Solution Set
    9	4,2,3; 5,3,1; 6,1,2
    9	4,3,2; 6,2,1; 5,1,3
    10	2,3,5; 4,5,1; 6,1,3
    10	2,5,3; 6,3,1; 4,1,5
    11	1,4,6; 3,6,2; 5,2,4
    11	1,6,4; 5,4,2; 3,2,6
    12	1,5,6; 2,6,4; 3,4,5
    12	1,6,5; 3,5,4; 2,4,6
    
    By concatenating each group it is possible to form 9-digit strings; the
    maximum string for a 3-gon ring is 432621513.

    Using the numbers 1 to 10, and depending on arrangements, it is possible to
    form 16- and 17-digit strings. What is the maximum 16-digit string for a
    "magic" 5-gon ring?
    """
    solutions = []
    for numbers in itertools.permutations(range(1, 11)):
        if 10 in numbers[len(numbers) / 2:]: continue # 17 digit string
        result = magic_string(numbers)
        if result:
            solutions.append(''.join(map(str, result)))
    return max(solutions)
