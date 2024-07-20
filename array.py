
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


def maximum_product_subarray_152(nums):
    """
    Given an integer array nums, find a subarray that has the largest product, and return the product.
    The test cases are generated so that the answer will fit in a 32-bit integer.

    Example 1:
    -----------
    Input: nums = [2,3,-2,4]
    Output: 6
    Explanation: [2,3] has the largest product 6.

    Example 2:
    -----------
    Input: nums = [-2,0,-1]
    Output: 0
    Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

    Constraints:
    -------------
    1 <= nums.length <= 2 * 104
    -10 <= nums[i] <= 10
    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
    """
    res = max(nums)
    cmax = 1
    cmin = 1

    for n in nums:

        if n == 0:
            cmax = 1
            cmin = 1
            continue

        vals = (n, n * cmax, n * cmin)
        cmax = max(vals)
        cmin = min(vals)

        res = max(res, cmax)
    return res


def container_with_most_water_11(height):
    """
    You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
    Find two lines that together with the x-axis form a container, such that the container contains the most water.
    Return the maximum amount of water a container can store.
    Notice that you may not slant the container.

    Example 1:
    -----------
    Input: height = [1,8,6,2,5,4,8,3,7]
    Output: 49
    Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

    Example 2:
    ----------
    Input: height = [1,1]
    Output: 1

    Constraints:
    --------------
    n == height.length
    2 <= n <= 105
    0 <= height[i] <= 104
    """
    max_vol = 0
    p1 = 0
    p2 = len(height) - 1
    while p1 < p2:
        curr_vol = min(height[p1], height[p2]) * (p2 - p1)
        if curr_vol > max_vol:
            max_vol = curr_vol
        if height[p1] > height[p2]:
            p2 -= 1
        else:
            p1 += 1
    return max_vol


def find_minimum_in_rotated_sorted_array_153(nums):
    """Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

    [4,5,6,7,0,1,2] if it was rotated 4 times.
    [0,1,2,4,5,6,7] if it was rotated 7 times.
    Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

    Given the sorted rotated array nums of unique elements, return the minimum element of this array.

    You must write an algorithm that runs in O(log n) time.

    Example 1:
    --------
    Input: nums = [3,4,5,1,2]
    Output: 1
    Explanation: The original array was [1,2,3,4,5] rotated 3 times.

    Example 2:
    ----------
    Input: nums = [4,5,6,7,0,1,2]
    Output: 0
    Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

    Example 3:
    ----------
    Input: nums = [11,13,15,17]
    Output: 11
    Explanation: The original array was [11,13,15,17] and it was rotated 4 times.

    Constraints:
    ------------
    n == nums.length
    1 <= n <= 5000
    -5000 <= nums[i] <= 5000
    All the integers of nums are unique.
    nums is sorted and rotated between 1 and n times.
    """
    l = 0
    r = len(nums) - 1
    res = nums[0]

    while l <= r:
        if nums[l] <= nums[r]:
            res = min(res, nums[l])
            break
        m = (l + r) // 2
        res = min(res, nums[m])  # m could be min

        # for next iter
        if nums[m] >= nums[l]:
            l += 1
        else:
            r -= 1

    return res