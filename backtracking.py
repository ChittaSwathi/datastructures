def letter_combinations_of_a_phone_number_17(digits):
    """
    Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

    A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

    Example 1:
    ------------
    Input: digits = "23"
    Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

    Example 2:
    -------------
    Input: digits = ""
    Output: []

    Example 3:
    -------------
    Input: digits = "2"
    Output: ["a","b","c"]

    Constraints:
    -------------
    0 <= digits.length <= 4
    digits[i] is a digit in the range ['2', '9'].
    """
    if not digits: return []

    res = []
    letters = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    def btrack(comb, digits):
        nonlocal res
        if len(digits) == 0:
            res.append(comb)
        else:
            for letter in letters[digits[0]]:
                btrack(comb + letter, digits[1:])

    btrack("", digits)
    return res
