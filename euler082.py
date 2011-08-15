
import heapq
import itertools

matrix, visited = [], set()

# note: uses the same input as 81
with open('euler081_input.txt') as f:
    matrix = [map(int, line.strip().split(',')) for line in f.readlines()]

def neighbors(x, y):
    dimy, dimx = len(matrix[0]), len(matrix)
    xs = [x, x + 1]
    ys = [y, y - 1, y + 1]
    def legal_neighbor((nx, ny)):
        global visited
        return 0 <= nx < dimx and \
                0 <= ny < dimy and \
                abs(nx + ny - (x + y)) == 1 and \
                (nx, ny) not in visited
    return filter(legal_neighbor, itertools.product(xs, ys))

def shortest_path(start, goal):
    global matrix, visited
    visited, q = set(), []
    heapq.heappush(q, (matrix[start[1]][start[0]], [start]))
    while len(q) > 0:
        cost, path = heapq.heappop(q)
        if path[-1][0] == len(matrix)-1: return cost
        if path[-1] in visited: continue
        visited.add(path[-1])
        for n in neighbors(*path[-1]):
            if n not in visited:
                new_path = path[:] + [n]
                heapq.heappush(q, (cost + matrix[n[1]][n[0]], new_path))


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
    global matrix
    return min([shortest_path((0, i), (len(matrix[0])-1, 0))
            for i in xrange(len(matrix))])

