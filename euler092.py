
def square_sum(n):
    sq_sum = 0
    while n > 0:
        sq_sum, n = sq_sum + (n%10)**2, n/10
    return sq_sum

def iterated_square_sum(n):
    while n != 1 and n != 89:
        n = square_sum(n)
    return n == 89

def euler92(upper_bound=10000000):
    """http://projecteuler.net/problem=92

    A number chain is created by continuously adding the square of the digits in
    a number to form a new number until it has been seen before.

    For example,

    44 → 32 → 13 → 10 → 1 → 1
    85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

    Therefore any chain that arrives at 1 or 89 will become stuck in an endless
    loop. What is most amazing is that EVERY starting number will eventually
    arrive at 1 or 89.

    How many starting numbers below ten million will arrive at 89?
    """
    # note: the maximum square sum for numbers under 10M is 567 (7 * 9**2)
    memo = map(iterated_square_sum, xrange(1, 568))
    return sum(1 for x in range(1, upper_bound) if memo[square_sum(x)-1])

