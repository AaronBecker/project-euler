
from euler_util import product

def count_rectangles(xdim, ydim):
    rects = 0
    for rectx in xrange(1, xdim+1):
        for recty in xrange(1, ydim+1):
            rects += (xdim - rectx + 1) * (ydim - recty + 1)
    return rects

def find_grid(target):
    best_x, best_y, best_score = 0, 0, target
    x, y = int(target**0.5), 1
    while x > 0:
        rects = count_rectangles(x, y)
        result = abs(target - rects)
        if result < best_score:
            best_x, best_y, best_score = x, y, result
        if rects > target:
            x = x - 1
        else:
            y = y + 1
    return best_x, best_y

def euler85(target=2000000):
    """http://projecteuler.net/index.php?section=problems&id=85

    By counting carefully it can be seen that a rectangular grid measuring 3 by
    2 contains eighteen rectangles.

    Although there exists no rectangular grid that contains exactly two million
    rectangles, find the area of the grid with the nearest solution."""
    return product(find_grid(target))
