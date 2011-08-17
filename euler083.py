
import itertools
from euler_util import shortest_path

# note: uses the same input as 81
with open('euler081_input.txt') as f:
    matrix = [map(int, line.strip().split(',')) for line in f.readlines()]


def neighbors((x, y)):
    dimy, dimx = len(matrix[0]), len(matrix)
    xs = [x, x - 1, x + 1]
    ys = [y, y - 1, y + 1]
    def legal_neighbor((nx, ny)):
        return 0 <= nx < dimx and \
                0 <= ny < dimy and \
                abs(nx + ny - (x + y)) == 1
    return filter(legal_neighbor, itertools.product(xs, ys))


def weight((x, y)):
    global matrix
    return matrix[y][x]


def goal((x, y)):
    global matrix
    return (x, y) == (len(matrix)-1, len(matrix[0])-1)


def euler83():
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
    return shortest_path((0, 0), neighbors, weight, goal)[0]

