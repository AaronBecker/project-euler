
import itertools

# note: uses the same input as 81
with open('euler081_input.txt') as f:
    matrix = [map(int, line.strip().split(',')) for line in f.readlines()]
    visited = set()

def neighbors(x, y):
    dimx, dimy = len(matrix[0]), len(matrix)
    xs = [x, x + 1]
    ys = [y, y - 1, y + 1]
    def legal_neighbor(nx, ny):
        global visited
        return 0 <= nx < dimx and \
                0 <= ny < dimy and nx + ny - (x + y) == 1 and \
                (nx, ny) not in visited
    return filter(legal_neighbor, itertools.product(xs, ys))


def shortest_path(path, goal):
    pass

def euler82():
    """http://projecteuler.net/index.php?section=problems&id=82

    The minimal path sum in the 5 by 5 matrix below, by starting in any cell in
    the left column and finishing in any cell in the right column, and only
    moving up, down, and right, is indicated in red and bold; the sum is equal
    to 994.

    131	673	234*103*18
    201*96**342	965	150
    630	803	746	422	111
    537	699	497	121	956
    805	732	524	37	331

    Find the minimal path sum, in matrix.txt (right click and 'Save Link/Target
    As...'), a 31K text file containing a 80 by 80 matrix, from the left column
    to the right column.
    """

