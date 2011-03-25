
coins = [1, 2, 5, 10, 20, 50, 100, 200]

def euler31(target=200):
    #FIXME: needs to be order-invariant
    """How many different ways can 2 GBP be made using any number of coins?"""
    memo = {0:1}
    for i in range(1, target+1):
        ways = 0
        for c in coins:
            if memo.has_key(i-c):
                ways = ways + memo[i-c]
        memo[i] = ways
    print "There are %d ways to make %d p from change" % (target, memo[target])
    return memo[target]
