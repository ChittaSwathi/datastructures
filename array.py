
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