
def euler45():
    """After 40755, what is the next triangle number 
    that is also pentagonal and hexagonal?"""
    triangles = set([n * (n + 1) / 2 for n in range(2, 100000)])
    pentangles = set([n * (3*n - 1) / 2 for n in range(2, 100000)])
    hexangles = set([n * (2*n - 1) for n in range(2, 100000)])
    common = triangles & pentangles & hexangles
    print common
    return common
