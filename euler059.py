
import itertools

def decrypt(text, key):
    dlist = []
    for i in xrange(len(text)):
        dlist.append(chr(ord(text[i]) ^ ord(key[i % 3])))
        if not 32 <= ord(dlist[-1]) <= ord('z'): return -1
    dtext = ''.join(dlist)
    if dtext.find(' the ') != -1:
        return sum(ord(d) for d in dtext)
    else:
        return -1


pe59 = eval('"".join(map(chr, [' +
        open('euler059_input.txt').readlines()[0].strip() + ']))')
def euler59(text=pe59):
    """http://projecteuler.net/problem=59

    Each character on a computer is assigned a unique code and the preferred
    standard is ASCII (American Standard Code for Information Interchange). For
    example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

    A modern encryption method is to take a text file, convert the bytes to
    ASCII, then XOR each byte with a given value, taken from a secret key. The
    advantage with the XOR function is that using the same encryption key on the
    cipher text, restores the plain text; for example, 65 XOR 42 = 107, then 107
    XOR 42 = 65.

    For unbreakable encryption, the key is the same length as the plain text
    message, and the key is made up of random bytes. The user would keep the
    encrypted message and the encryption key in different locations, and without
    both "halves", it is impossible to decrypt the message.

    Unfortunately, this method is impractical for most users, so the modified
    method is to use a password as a key. If the password is shorter than the
    message, which is likely, the key is repeated cyclically throughout the
    message. The balance for this method is using a sufficiently long password
    key for security, but short enough to be memorable.

    Your task has been made easy, as the encryption key consists of three lower
    case characters. Using cipher1.txt (right click and 'Save Link/Target
    As...'), a file containing the encrypted ASCII codes, and the knowledge that
    the plain text must contain common English words, decrypt the message and
    find the sum of the ASCII values in the original text.
    """
    # note: key is known to be 3 letters, lower case
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for key in itertools.product(alphabet, alphabet, alphabet):
        val = decrypt(text, key)
        if val != -1: return val
