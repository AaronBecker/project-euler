
from numpy import array, cross, dot

def shares_side(p, q, a, b):
    return dot(cross(b-a, p-a), cross(b-a, q-a)) >= 0

origin = array([0, 0])
def origin_in_triangle(a, b, c):
    return shares_side(origin, a, b, c) and \
            shares_side(origin, b, a, c) and \
            shares_side(origin, c, a, b)

with open('euler102_input.txt') as f:
    pe102 = [map(int, line.strip().split(',')) for line in f.readlines()]

def euler102(triangles=pe102):
    """http://projecteuler.net/index.php?section=problems&id=102

    For how many triangles in the text file does the interior contain the
    origin?"""
    return sum(origin_in_triangle(array(tri[0:2]), array(tri[2:4]),
        array(tri[4:6])) for tri in triangles)

