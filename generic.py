
def palindrome_number_9(x):
    """Given an integer x, return true if x is a palindrome, and false otherwise.

    Example 1:
    -------------
    Input: x = 121
    Output: true
    Explanation: 121 reads as 121 from left to right and from right to left.

    Example 2:
    -------------
    Input: x = -121
    Output: false
    Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

    Example 3:
    -------------
    Input: x = 10
    Output: false
    Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

    Constraints:
    -------------
    -231 <= x <= 231 - 1

    Follow up: Could you solve it without converting the integer to a string?"""

    # brute force - converting number to string
    return True if str(x) == str(x)[::-1] else False

    #optimized - reverse number calc
    if x < 0:
        return False
    reverse = 0
    temp = x
    while temp != 0:
        digit = temp % 10
        reverse = reverse * 10 + digit
        temp = temp // 10
    return x == reverse