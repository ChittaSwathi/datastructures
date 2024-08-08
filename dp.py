
def n_th_tribonacci_number_1137(n):
    """
    The Tribonacci sequence Tn is defined as follows:

    T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

    Given n, return the value of Tn.

    Example 1:
    -------------
    Input: n = 4
    Output: 4
    Explanation:
    T_3 = 0 + 1 + 1 = 2
    T_4 = 1 + 1 + 2 = 4

    Example 2:
    ------------
    Input: n = 25
    Output: 1389537

    Constraints:
    ---------------
    0 <= n <= 37
    The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1.
    """
    if not n: return 0
    memo = {0: 0, 1: 1, 2: 1}

    def fib(n):
        if n in memo:
            return memo[n]
        else:
            res = fib(n - 1) + fib(n - 2) + fib(n - 3)
            memo[n] = res
            return res

    return fib(n)


def climbing_stairs_70(n):
    """You are climbing a staircase. It takes n steps to reach the top.

    Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

    Example 1:
    ----------
    Input: n = 2
    Output: 2
    Explanation: There are two ways to climb to the top.
    1. 1 step + 1 step
    2. 2 steps

    Example 2:
    ----------
    Input: n = 3
    Output: 3
    Explanation: There are three ways to climb to the top.
    1. 1 step + 1 step + 1 step
    2. 1 step + 2 steps
    3. 2 steps + 1 step

    Constraints:
    ------------
    1 <= n <= 45"""
    def climb(n, memo):
        if n in memo:
            return memo[n]
        memo[n] = climb(n - 1, memo) + climb(n - 2, memo)
        return memo[n]

    memo = {0: 0, 1: 1, 2: 2}
    return climb(n, memo)


def min_cost_climbing_stairs_746(cost):
    """You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

    You can either start from the step with index 0, or the step with index 1.

    Return the minimum cost to reach the top of the floor.

    Example 1:
    --------------
    Input: cost = [10,15,20]
    Output: 15
    Explanation: You will start at index 1.
    - Pay 15 and climb two steps to reach the top.
    The total cost is 15.

    Example 2:
    ------------
    Input: cost = [1,100,1,1,1,100,1,1,100,1]
    Output: 6
    Explanation: You will start at index 0.
    - Pay 1 and climb two steps to reach index 2.
    - Pay 1 and climb two steps to reach index 4.
    - Pay 1 and climb two steps to reach index 6.
    - Pay 1 and climb one step to reach index 7.
    - Pay 1 and climb two steps to reach index 9.
    - Pay 1 and climb one step to reach the top.
    The total cost is 6.

    Constraints:
    ----------------
    2 <= cost.length <= 1000
    0 <= cost[i] <= 999"""
    if not cost: return 0

    memo = [0] * len(cost)
    memo[0] = cost[0]
    if len(cost) >= 2: memo[1] = cost[1]

    for i in range(2, len(cost)):
        memo[i] = cost[i] + min(memo[i - 1], memo[i - 2])

    return min(memo[-1], memo[-2])


def house_robber_198(nums):
    """You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

    Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

    Example 1:
    --------------
    Input: nums = [1,2,3,1]
    Output: 4
    Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
    Total amount you can rob = 1 + 3 = 4.

    Example 2:
    --------------
    Input: nums = [2,7,9,3,1]
    Output: 12
    Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
    Total amount you can rob = 2 + 9 + 1 = 12.

    Constraints:
    ---------------
    1 <= nums.length <= 100
    0 <= nums[i] <= 400"""

    if not nums:
        return 0

    if len(nums) == 1:
        return nums[0]

    memo = [0] * len(nums)
    memo[0] = nums[0]
    if len(nums) >= 2:
        memo[1] = max(nums[0], nums[1])

    for i in range(2, len(nums)):
        memo[i] = max(memo[i-1], nums[i] + memo[i-2])

    return memo[-1]



def decode_ways_91(s):
    """
    You have intercepted a secret message encoded as a string of numbers. The message is decoded via the following mapping:
    "1" -> 'A'
    "2" -> 'B'
    ...
    "25" -> 'Y'
    "26" -> 'Z'

    However, while decoding the message, you realize that there are many different ways you can decode the message because some codes are contained in other codes ("2" and "5" vs "25").
    For example, "11106" can be decoded into:
    "AAJF" with the grouping (1, 1, 10, 6)
    "KJF" with the grouping (11, 10, 6)
    The grouping (1, 11, 06) is invalid because "06" is not a valid code (only "6" is valid).
    Note: there may be strings that are impossible to decode.

    Given a string s containing only digits, return the number of ways to decode it. If the entire string cannot be decoded in any valid way, return 0.
    The test cases are generated so that the answer fits in a 32-bit integer.

    Example 1:
    -----------
    Input: s = "12"
    Output: 2
    Explanation:
    "12" could be decoded as "AB" (1 2) or "L" (12).

    Example 2:
    ------------
    Input: s = "226"
    Output: 3
    Explanation:
    "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

    Example 3:
    -----------
    Input: s = "06"
    Output: 0
    Explanation:
    "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06"). In this case, the string is not a valid encoding, so return 0.

    Constraints:
    --------------
    1 <= s.length <= 100
    s contains only digits and may contain leading zero(s).
    """

    # only dp solution
    dp = [0] * (len(s) + 1)
    # dp[i] denotes decodings till s[i-1]; so dp[i] is dependent on dp[i-1] and dp[i-2]
    dp[0] = 1
    dp[1] = 1

    if s[0] == '0': return 0

    for i in range(2, len(s) + 1):
        if 1 <= int(s[i - 1]) <= 9: #checking current single char is between 1 and 9
            dp[i] += dp[i - 1]
        if 10 <= int(s[i - 2] + s[i - 1]) <= 26: # checking if two digit val lies between 10 and 26
            dp[i] += dp[i - 2]

    return dp[-1]

    # dp with dfs solution
    dp = {len(s): 1}

    def dfs(i):
        if i in dp:
            return dp[i]
        if s[i] == '0':
            return 0

        res = dfs(i + 1)
        if i+1 < len(s) and 10<= int(s[i]+s[i+1]) <= 26:
            # checking if two digit val lies between 10 and 26
            res += dfs(i + 2)
        dp[i] = res
        return res

    return dfs(0)