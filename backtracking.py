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


def combination_sum_iii_216(k, n):
    """
    Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

    Only numbers 1 through 9 are used.
    Each number is used at most once.
    Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.

    Example 1:
    -----------
    Input: k = 3, n = 7
    Output: [[1,2,4]]
    Explanation:
    1 + 2 + 4 = 7
    There are no other valid combinations.

    Example 2:
    --------------
    Input: k = 3, n = 9
    Output: [[1,2,6],[1,3,5],[2,3,4]]
    Explanation:
    1 + 2 + 6 = 9
    1 + 3 + 5 = 9
    2 + 3 + 4 = 9
    There are no other valid combinations.

    Example 3:
    -------------
    Input: k = 4, n = 1
    Output: []
    Explanation: There are no valid combinations.
    Using 4 different numbers in the range [1,9], the smallest sum we can get is 1+2+3+4 = 10 and since 10 > 1, there are no valid combination.

    Constraints:
    ------------
    2 <= k <= 9
    1 <= n <= 60
    """
    res = []

    def backtrack(start, nums, sum):
        print(start, nums)
        if len(nums) == k:
            if sum == n:
                res.append(nums)
            return

        for i in range(start, 10):
            backtrack(i + 1, nums + [i], sum + i)

    backtrack(1, [], 0)
    return res
