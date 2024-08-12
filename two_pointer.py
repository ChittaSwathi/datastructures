def move_zeroes_283():
    """
    Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
    Note that you must do this in-place without making a copy of the array.

    Example 1:
    ------------
    Input: nums = [0,1,0,3,12]
    Output: [1,3,12,0,0]
    
    Example 2:
    ------------
    Input: nums = [0]
    Output: [0]

    Constraints:
    --------------
    1 <= nums.length <= 104
    -231 <= nums[i] <= 231 - 1
    """
    
    # two pointer approach
    if not nums or len(nums) == 1: 
        return nums
    l = 0
    for r in range(len(nums)):
        if nums[l] == 0 and nums[r] != 0: #if left is zero and right is not zero, swap
            nums[l], nums[r] = nums[r], nums[l]
        if nums[l] != 0:
            l += 1
        


def container_with_most_water_11(height):
    """
    You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
    Find two lines that together with the x-axis form a container, such that the container contains the most water.
    Return the maximum amount of water a container can store.
    Notice that you may not slant the container.

    Example 1:
    ----------
    Input: height = [1,8,6,2,5,4,8,3,7]
    Output: 49
    Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
    
    Example 2:
    ------------
    Input: height = [1,1]
    Output: 1
    
    Constraints:
    --------------
    n == height.length
    2 <= n <= 105
    0 <= height[i] <= 104
    """
    return None
