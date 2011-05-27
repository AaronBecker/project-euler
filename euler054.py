
def suit(c):
    return c[1]

def rank(c):
    return int(c[0]) if c[0].isdigit() else rank.values[c[0]]
rank.values = { 'T' : 10, 'J' : 11, 'Q' : 12, 'K' : 13, 'A' : 14 }

def two_pair(sets):
    return sets[0][0] == 2 and sets[1][0] == 2

def three_of_a_kind(sets):
    return sets[0][0] == 3

def straight(hand):
    ranks = sorted([rank(c) for c in hand])
    return len(set(ranks)) == 5 and ranks[-1] - ranks[0] == 4

def flush(hand):
    suits = set([suit(c) for c in hand])
    return len(suits) == 1

def full_house(sets):
    return sets[0][0] == 3 and sets[1][0] == 2

def four_of_a_kind(sets):
    return sets[0][0] == 4

def straight_flush(hand):
    return straight(hand) and flush(hand)

def value(hand):
    sets = []
    for r in xrange(2, 15):
        sets.append((sum(1 for c in hand if rank(c) == r), r))
    sets = sorted(sets, reverse=True)
    return [straight_flush(hand), four_of_a_kind(sets),
            full_house(sets), flush(hand), straight(hand),
            three_of_a_kind(sets), two_pair(sets)] + sets

with open('euler054_input.txt') as f:
    pe54 = [line.strip().split() for line in f.readlines()]

def euler54(hands=pe54):
    """http://projecteuler.net/index.php?section=problems&id=54

    In the card game poker, a hand consists of five cards and are ranked, from
    lowest to highest, in the following way:

    High Card: Highest value card.
    One Pair: Two cards of the same value.
    Two Pairs: Two different pairs.
    Three of a Kind: Three cards of the same value.
    Straight: All cards are consecutive values.
    Flush: All cards of the same suit.
    Full House: Three of a kind and a pair.
    Four of a Kind: Four cards of the same value.
    Straight Flush: All cards are consecutive values of same suit.
    Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
    The cards are valued in the order:
    2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

    If two players have the same ranked hands then the rank made up of the
    highest value wins; for example, a pair of eights beats a pair of fives
    (see example 1 below). But if two ranks tie, for example, both players have
    a pair of queens, then highest cards in each hand are compared (see example
    4 below); if the highest cards tie then the next highest cards are
    compared, and so on.

    The file, poker.txt, contains one-thousand random hands dealt to two
    players. Each line of the file contains ten cards (separated by a single
    space): the first five are Player 1's cards and the last five are Player
    2's cards. You can assume that all hands are valid (no invalid characters
    or repeated cards), each player's hand is in no specific order, and in each
    hand there is a clear winner.

    How many hands does Player 1 win?"""
    return sum(1 for hand in hands if value(hand[:5]) > value(hand[5:]))

