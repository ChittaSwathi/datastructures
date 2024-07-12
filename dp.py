
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

