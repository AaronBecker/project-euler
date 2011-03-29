from euler_util import is_palindrome

def euler55():
    """http://projecteuler.net/index.php?section=problems&id=55
    
    How many Lychrel numbers are there below ten-thousand?"""
    lychrel = []
    for n in range(10000):
        candidate = n
        is_lychrel = True
        for round in range(50):
            candidate += int(str(candidate)[::-1])
            if is_palindrome(candidate):
                is_lychrel = False
                break
        if is_lychrel: lychrel.append(n)
    return len(lychrel)
