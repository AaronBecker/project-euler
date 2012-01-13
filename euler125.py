
from euler_util import is_palindrome

def euler125(upper_bound=10**8):
    """http://projecteuler.net/problem=125

    The palindromic number 595 is interesting because it can be written as the
    sum of consecutive squares: 6^2 + 7^2 + 8^2 + 9^2 + 10^2 + 11^2 + 12^2.

    There are exactly eleven palindromes below one-thousand that can be written
    as consecutive square sums, and the sum of these palindromes is 4164. Note
    that 1 = 0^2 + 1^2 has not been included as this problem is concerned with
    the squares of positive integers.

    Find the sum of all the numbers less than 108 that are both palindromic and
    can be written as the sum of consecutive squares.
    """
    top_square = int(upper_bound**0.5)
    square_sums = [0]*top_square
    for i in xrange(1, top_square):
        square_sums[i] = square_sums[i-1] + i*i

    answers = {}
    for i in xrange(1, len(square_sums)):
        for j in xrange(i-1):
            if is_palindrome(square_sums[i] - square_sums[j]):
                answers[square_sums[i] - square_sums[j]] = True
    #results = sorted([n for n in answers.keys() if n < upper_bound])
    #print results
    return sum([n for n in answers.keys() if n < upper_bound])
