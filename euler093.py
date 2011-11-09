
from operator import add, sub, mul, div
from itertools import permutations, combinations, combinations_with_replacement

# Since we are only working with length 4 sequences, we don't have to worry
# about arbitrary tree structures. Instead, we can just rely on ordering of
# operands and special-case the only situation where parenthesization can give
# a result not equivalent to evalating some sequence of digit ops in order from
# start to finish (via eval_list2).
def eval_list(digits, ops):
    total = float(digits[0])
    for i in range(len(ops)):
        total = ops[i](total, digits[i+1])
    if abs(total - int(total)) > 10**-5:
        total = 0
    else:
        total = int(round(total))
    return max(total, 0)

def eval_list2(digits, ops):
    total = ops[0](float(digits[0]), float(digits[1]))
    total = ops[1](total, ops[2](float(digits[2]), float(digits[3])))
    if abs(total - int(total)) > 10**-5:
        total = 0
    else:
        total = int(round(total))
    return max(total, 0)
    
def results_from_ordered_digits(digits):
    results = set()
    operations = [add, sub, mul, div]
    for ops in combinations_with_replacement(operations, 3):
        for ordered_ops in permutations(ops):
            results.add(eval_list(digits, ordered_ops))
            results.add(eval_list2(digits, ordered_ops))
    return results

def possible_results(inputs):
    results = set()
    for digits in permutations(inputs):
        results = results.union(results_from_ordered_digits(digits))
    return results

def first_missing_result(inputs):
    i, results = 0, list(possible_results(inputs))
    while results[i] == i:
        i += 1
    return i

def euler93():
    """http://projecteuler.net/index.php?section=problems&id=93"""
    inputs = list(combinations(range(1, 10), 4))
    #print sorted(zip(map(first_missing_result, inputs), inputs))
    digits = max(zip(map(first_missing_result, inputs), inputs))[1]
    return ''.join(map(str, digits))
