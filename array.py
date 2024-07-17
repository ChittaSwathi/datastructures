
def find_pivot_index_724(nums):
    """
    Given an array of integers nums, calculate the pivot index of this array.
    The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.
    If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.
    Return the leftmost pivot index. If no such index exists, return -1.

    Example 1:
    ------------
    Input: nums = [1,7,3,6,5,6]
    Output: 3
    Explanation:
    The pivot index is 3.
    Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
    Right sum = nums[4] + nums[5] = 5 + 6 = 11

    Example 2:
    -----------
    Input: nums = [1,2,3]
    Output: -1
    Explanation:
    There is no index that satisfies the conditions in the problem statement.

    Example 3:
    -----------
    Input: nums = [2,1,-1]
    Output: 0
    Explanation:
    The pivot index is 0.
    Left sum = 0 (no elements to the left of index 0)
    Right sum = nums[1] + nums[2] = 1 + -1 = 0

    Constraints:
    ------------
    1 <= nums.length <= 104
    -1000 <= nums[i] <= 1000

    """

    left_sum = 0
    right_sum = sum(nums)

    for idx, ele in enumerate(nums):
        right_sum -= ele
        if left_sum == right_sum:
            return idx

        left_sum += ele
    return -1


def find_the_highest_altitude_1732(gain):
    """
    There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. The biker starts his trip on point 0 with altitude equal 0.

    You are given an integer array gain of length n where gain[i] is the net gain in altitude between points and i + 1 for all (0 <= i < n). Return the highest altitude of a point.

    Example 1:
    -----------
    Input: gain = [-5,1,5,0,-7]
    Output: 1
    Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.

    Example 2:
    -----------
    Input: gain = [-4,-3,-2,-1,4,3,2]
    Output: 0
    Explanation: The altitudes are [0,-4,-7,-9,-10,-6,-3,-1]. The highest is 0.

    Constraints:
    -------------
    n == gain.length
    1 <= n <= 100
    -100 <= gain[i] <= 100
    """

    res = [0]
    for i in gain:
        res.append(res[-1]+i)
    return max(res)


def product_of_array_except_self_238(nums):
    """
    Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

    You must write an algorithm that runs in O(n) time and without using the division operation.

    Example 1:
    ----------
    Input: nums = [1,2,3,4]
    Output: [24,12,8,6]

    Example 2:
    ------------
    Input: nums = [-1,1,0,-3,3]
    Output: [0,0,9,0,0]

    Constraints:
    -------------
    2 <= nums.length <= 105
    -30 <= nums[i] <= 30
    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
    """

    n = len(nums)

    left = [1] * n
    right = [1] * n

    for i in range(1, n):  # not calculating the first index val
        left[i] = left[i - 1] * nums[i - 1]

    for i in range(n - 2, -1, -1):  # not calculating the kast index val
        right[i] = right[i + 1] * nums[i + 1]

    return [left[i] * right[i] for i in range(n)]


def two_sum_1(nums, target):
    """
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    You can return the answer in any order.

    Example 1:
    -----------
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

    Example 2:
    ------------
    Input: nums = [3,2,4], target = 6
    Output: [1,2]

    Example 3:
    -------------
    Input: nums = [3,3], target = 6
    Output: [0,1]

    Constraints:
    -------------
    2 <= nums.length <= 104
    -109 <= nums[i] <= 109
    -109 <= target <= 109
    Only one valid answer exists.
    """

    memo = {}
    for key, val in enumerate(nums):
        res = target - val
        if res in memo:
            return [memo[res], key]
        memo[val] = key
    return []


def best_time_to_buy_and_sell_stock_121(prices):
    """
    You are given an array prices where prices[i] is the price of a given stock on the ith day.

    You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

    Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

    Example 1:
    -----------
    Input: prices = [7,1,5,3,6,4]
    Output: 5
    Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
    Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

    Example 2:
    -----------
    Input: prices = [7,6,4,3,1]
    Output: 0
    Explanation: In this case, no transactions are done and the max profit = 0.

    Constraints:
    -------------
    1 <= prices.length <= 105
    0 <= prices[i] <= 104
    """

    min_price = prices[0]
    max_profit = 0

    for price in prices:
        max_profit = max(max_profit, price - min_price)
        min_price = min(min_price, price)

    return max_profit


def contains_duplicate_217(nums):
    """
    Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

    Example 1:
    -------------
    Input: nums = [1,2,3,1]
    Output: true

    Example 2:
    --------------
    Input: nums = [1,2,3,4]
    Output: false

    Example 3:
    -------------
    Input: nums = [1,1,1,3,3,4,3,2,4,2]
    Output: true

    Constraints:
    --------------
    1 <= nums.length <= 105
    -109 <= nums[i] <= 109
    """
    memo = set()
    for i in nums:
        if i in memo:
            return True
        else:
            memo.add(i)
    return False


def maximum_subarray_53(nums):
    """
    Given an integer array nums, find the subarray with the largest sum, and return its sum.

    Example 1:
    ------------
    Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
    Output: 6
    Explanation: The subarray [4,-1,2,1] has the largest sum 6.

    Example 2:
    -------------
    Input: nums = [1]
    Output: 1
    Explanation: The subarray [1] has the largest sum 1.

    Example 3:
    --------------
    Input: nums = [5,4,-1,7,8]
    Output: 23
    Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

    Constraints:
    --------------
    1 <= nums.length <= 105
    -104 <= nums[i] <= 104
    """

    max_sum = float("-inf")
    curr_sum = 0

    for num in nums:
        curr_sum += num

        if curr_sum > max_sum:
            max_sum = curr_sum

        if curr_sum < 0:
            curr_sum = 0

    return max_sum
