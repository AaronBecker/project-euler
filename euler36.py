from euler_util import is_palindrome

def to_binary(x):
    """Convert an int to its base 2 string equivalent"""
    if x == 0: return '0'
    b = ''
    if x < 0: x *= -1
    while x > 0:
        b = str(x&1) + b
        x >>= 1
    return b

def euler36(upper_bound=10 ** 6):
    """Find the sum of all numbers, less than one million,
    which are palindromic in base 10 and base 2."""
    p_sum = 0
    # note: we can skip even numbers since they're never binary palindromes
    for n in range(1, upper_bound, 2):
        if is_palindrome(n) and is_palindrome(to_binary(n)): p_sum += n
    print 'The sum of all numbers under %d which are palindromic in both'\
            ' decimal and binary is %d' % (upper_bound, p_sum)
    return p_sum
