
with open('euler081_input.txt') as f:
    pe81 = [map(int, line.strip().split(',')) for line in f.readlines()]

def euler81(matrix=pe81):
    """http://projecteuler.net/index.php?section=problems&id=81

    Find the minimal path sum from the top left to the bottom right by moving
    right and down."""
    shortest_path = [[matrix[0][0]]*len(matrix[0]) for n in xrange(len(matrix))]
    for n in xrange(1, len(matrix[0])):
        shortest_path[0][n] = matrix[0][n] + shortest_path[0][n-1]
        shortest_path[n][0] = matrix[n][0] + shortest_path[n-1][0]
    for y in xrange(1, len(matrix[0])):
        for x in xrange(1, len(matrix)):
            shortest_path[x][y] = matrix[x][y] + \
                    min(shortest_path[x-1][y], shortest_path[x][y-1])
    return shortest_path[-1][-1]
