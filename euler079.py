
import itertools

keys = map(lambda x: x.strip(), open('euler079_input.txt').readlines())
digits = set(''.join(keys))

def key_is_valid(s, key):
    return -1 < s.find(key[0]) < s.find(key[1]) < s.find(key[2])

def euler79():
    """http://projecteuler.net/index.php?section=problems&id=79

    By analysing a user's login attempts, can you determine the secret numeric
    passcode?"""
    # note: assumes no repetition of password digits
    for i in itertools.permutations(digits):
        s = ''.join(i)
        if not set(s) <= digits: continue
        if all(map(lambda x: key_is_valid(s, x), keys)): return s

