
def euler17(upper_bound=1000):
    """http://projecteuler.net/index.php?section=problems&id=17
    
    How many letters would be needed to write all the numbers in words from 1
    to 1000?"""
    digits = {
            1: 3,
            2: 3,
            3: 5,
            4: 4,
            5: 4,
            6: 3,
            7: 5,
            8: 5,
            9: 4,
            0: 0
    }
    unique_numbers = { 
            10: 3,
            11: 6,
            12: 6,
            13: 8,
            15: 7,
            18: 8,
            1000: 11
    }
    tens_modifiers = {
            10: 4,
            20: 6,
            30: 6,
            40: 5,
            50: 5,
            60: 5,
            70: 7,
            80: 6,
            90: 6,
            0: 0
    }
    letter_sum = 0
    for i in range(1, 10):
        letter_sum += digits[i]
    for i in range(10, 100):
        if unique_numbers.has_key(i):
            letter_sum += unique_numbers[i]
        else:
            letter_sum += tens_modifiers[i - i % 10] + digits[i % 10]
    hundreds_sum = len("hundred")
    for i in range(100, 1000):
        letter_orig = letter_sum
        letter_sum += digits[i / 100]
        tens = tens_modifiers[i % 100 - i % 10] + digits[i % 10]
        if unique_numbers.has_key(i % 100): tens = unique_numbers[i % 100]
        if tens != 0:
            letter_sum += tens + hundreds_sum + 3
        else:
            letter_sum += hundreds_sum
    letter_sum += unique_numbers[1000]
    return letter_sum

