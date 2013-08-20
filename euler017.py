

def euler17(upper_bound=1000):
    """http://projecteuler.net/problem=17

    If the numbers 1 to 5 are written out in words: one, two, three, four,
    five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

    If all the numbers from 1 to 1000 (one thousand) inclusive were written out
    in words, how many letters would be used?

    NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
    forty-two) contains 23 letters and 115 (one hundred and fifteen) contains
    20 letters. The use of "and" when writing out numbers is in compliance with
    British usage.
    """
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
    letter_sum, hundreds_sum = 0, len("hundred")
    for i in range(1, 1001):
        if i in unique_numbers:
            letter_sum += unique_numbers[i]
        elif i < 10:
            letter_sum += digits[i]
        elif i < 100:
            letter_sum += tens_modifiers[i - i % 10] + digits[i % 10]
        else:
            letter_sum += digits[i / 100]
            tens = tens_modifiers[i % 100 - i % 10] + digits[i % 10]
            if i % 100 in unique_numbers:
                tens = unique_numbers[i % 100]
            if tens != 0:
                letter_sum += tens + hundreds_sum + 3
            else:
                letter_sum += hundreds_sum
    return letter_sum
