
def is_palindrome(candidate):
    """Determine whether or not a number (or any string) is palindromic"""
    digits = [digit for digit in str(candidate)]
    return (digits == digits[::-1])

def euler4(upper_bound=1000):
    """Find the largest palindrome made from the product of two 3-digit numbers."""
    max_pal = 0
    for x in xrange(0,1000):
        for y in xrange(0,1000):
            if x*y > max_pal and is_palindrome(x*y):
                max_pal = x*y
    print "The largest palindrome product of numbers under %d is %d\n" %\
            (upper_bound, max_pal)
    return max_pal

