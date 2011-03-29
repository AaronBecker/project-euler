
uk_coins = [1, 2, 5, 10, 20, 50, 100, 200]

def change_count(target, total, coin, coins):
    if total == target:
        return 1
    if total < target and len(coins) > 0 and coin <= coins[0]:
        return change_count(target, total + coins[0], coins[0], coins) + \
                change_count(target, total, coin, coins[1:])
    return 0

def euler31(target=200):
    """http://projecteuler.net/index.php?section=problems&id=31
    
    How many different ways can 2 GBP be made using any number of coins?"""
    return change_count(200, 0, 1, uk_coins)

