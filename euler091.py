
def forms_triangle(x1, y1, x2, y2):
    # The origin is the implicit third point.
    A = x1**2 + y1**2
    B = x2**2 + y2**2
    C = (x1-x2)**2 + (y1-y2)**2
    return A == B+C or B == A+C or C == A+B 

def euler91(upper_bound=51):
    """http://projecteuler.net/problem=91

    There are exactly fourteen triangles containing a right angle that can be
    formed when each co-ordinate lies between 0 and 2 inclusive; that is,
    0 <= x1, y1, x2, y2 <= 2.

    Given that 0 <= x1, y1, x2, y2 <= 50, how many right triangles can be
    formed?
    """
    # Just enumerate all possible pairs of points and check if each is a right
    # triangle.
    solutions = 0
    for x1 in range(upper_bound):
        for y1 in range(upper_bound):
            if x1 + y1 == 0: continue
            for x2 in range(upper_bound):
                for y2 in range(upper_bound):
                    if x2 + y2 == 0 or (x1, y1) == (x2, y2): continue
                    if forms_triangle(x1, y1, x2, y2): solutions += 1
    # Note: we're double-counting everything.
    return solutions / 2

    
