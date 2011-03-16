
def euler39(upper_bound=1000):
    """If p is the perimeter of a right angle triangle, {a, b, c}, 
    which value, for p <= 1000, has the most solutions?"""
    triples = {}
    max_length = 0
    max_perimeter = 0
    for m in range(1, upper_bound/2):
        for n in range(1, m):
            k = 1
            while True:
                a, b, c = 2*m*n*k, k*(m*m - n*n), k*(m*m + n*n)
                p = a + b + c
                if p > upper_bound: break
                if not triples.has_key(p):
                    triples[p] = set()
                triples[p].add((a,b,c))
                if len(triples[p]) > max_length:
                    max_length = len(triples[p])
                    max_perimeter = p
                k += 1
    print 'The following is the longest list of triples:'
    print list(triples[max_perimeter])
    print 'Attained when p = %d' % max_perimeter
    return max_perimeter
