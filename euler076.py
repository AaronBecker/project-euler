
def euler76(n=100):
    """http://projecteuler.net/problem=76

    It is possible to write five as a sum in exactly six different ways:

    4 + 1
    3 + 2
    3 + 1 + 1
    2 + 2 + 1
    2 + 1 + 1 + 1
    1 + 1 + 1 + 1 + 1

    How many different ways can one hundred be written as a sum of at least two
    positive integers?
    """
    # This is just the partition function. I actually "solved" it by looking
    # the number up on wikipedia, but here's Euler's generating function
    # for completeness.
    p = [1]
    for i in xrange(1, n + 1):
        j, k, s = 1, 1, 0
        while j > 0:
            j = i - (3 * k * k + k) // 2
            if j >= 0:
                s -= (-1) ** k * p[j]
            j = i - (3 * k * k - k) // 2
            if j >= 0:
                s -= (-1) ** k * p[j]
            k += 1
        p.append(s)
    return p[n] - 1
