
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

    #brute force
    memo = {}
    for key, val in enumerate(nums):
        res = target - val
        if res in memo:
            return [memo[res], key]
        memo[val] = key
    return []

    #optimized - using lookup dict - time- O(n)
    lookup = {}
    # create lookup dict
    for i in range(len(nums)):
        lookup[target - nums[i]] = i
    # use lookup dict
    for j in range(len(nums)):
        if nums[j] in lookup and lookup[nums[j]] != j:
            return [lookup[nums[j]], j]
    return []  # not found


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

def merge_strings_alternately_1768(word1, word2):
    """
    You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

    Return the merged string.

    Example 1:
    ------------
    Input: word1 = "abc", word2 = "pqr"
    Output: "apbqcr"
    Explanation: The merged string will be merged as so:
    word1:  a   b   c
    word2:    p   q   r
    merged: a p b q c r

    Example 2:
    -----------
    Input: word1 = "ab", word2 = "pqrs"
    Output: "apbqrs"
    Explanation: Notice that as word2 is longer, "rs" is appended to the end.
    word1:  a   b
    word2:    p   q   r   s
    merged: a p b q   r   s

    Example 3:
    -----------
    Input: word1 = "abcd", word2 = "pq"
    Output: "apbqcd"
    Explanation: Notice that as word1 is longer, "cd" is appended to the end.
    word1:  a   b   c   d
    word2:    p   q
    merged: a p b q c   d

    Constraints:
    -------------
    1 <= word1.length, word2.length <= 100
    word1 and word2 consist of lowercase English letters.
    """
    m = min([len(word1), len(word2)])
    res = ''
    for i in range(m):
        res += word1[i] + word2[i]
    res += word1[m:]
    res += word2[m:]
    return res

def greatest_common_divisor_of_strings_1071(str1, str2):
    """For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

    Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.
    
    Example 1:
    ------------
    Input: str1 = "ABCABC", str2 = "ABC"
    Output: "ABC"
    
    Example 2:
    -----------
    Input: str1 = "ABABAB", str2 = "ABAB"
    Output: "AB"
    
    Example 3:
    -----------
    Input: str1 = "LEET", str2 = "CODE"
    Output: ""
     
    Constraints:
    --------------
    1 <= str1.length, str2.length <= 1000
    str1 and str2 consist of English uppercase letters.
    """
    len1, len2 = len(str1), len(str2)

    for i in range(min(len1, len2), 0, -1):
        s1, s2 = len1//i, len2//i
        if str1[:i] * s1 == str1 and str1[:i] * s2 == str2:
            return str1[:i]

    return ""

def kids_with_the_greatest_number_of_candies_1431(candies, extraCandies):
    """
    There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.

    Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.

    Note that multiple kids can have the greatest number of candies.

    Example 1:
    ------------
    Input: candies = [2,3,5,1,3], extraCandies = 3
    Output: [true,true,true,false,true]
    Explanation: If you give all extraCandies to:
    - Kid 1, they will have 2 + 3 = 5 candies, which is the greatest among the kids.
    - Kid 2, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
    - Kid 3, they will have 5 + 3 = 8 candies, which is the greatest among the kids.
    - Kid 4, they will have 1 + 3 = 4 candies, which is not the greatest among the kids.
    - Kid 5, they will have 3 + 3 = 6 candies, which is the greatest among the kids.

    Example 2:
    -------------
    Input: candies = [4,2,1,1,2], extraCandies = 1
    Output: [true,false,false,false,false]
    Explanation: There is only 1 extra candy.
    Kid 1 will always have the greatest number of candies, even if a different kid is given the extra candy.

    Example 3:
    ------------
    Input: candies = [12,1,12], extraCandies = 10
    Output: [true,false,true]

    Constraints:
    -------------
    n == candies.length
    2 <= n <= 100
    1 <= candies[i] <= 100
    1 <= extraCandies <= 50
    """
    max_candy = max(candies)
    for i in range(len(candies)):
        if candies[i] + extraCandies >= max_candy:
            candies[i] = True
        else:
            candies[i] = False
    return candies


def can_place_flowers_605(flowerbed, n):
    """
    You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

    Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.



    Example 1:
    ------------
    Input: flowerbed = [1,0,0,0,1], n = 1
    Output: true

    Example 2:
    -----------
    Input: flowerbed = [1,0,0,0,1], n = 2
    Output: false

    Constraints:
    ------------
    1 <= flowerbed.length <= 2 * 104
    flowerbed[i] is 0 or 1.
    There are no two adjacent flowers in flowerbed.
    0 <= n <= flowerbed.length
    """
    flowerbed = [0] + flowerbed + [0]
    count = 0
    for i in range(1, len(flowerbed) - 1):
        if flowerbed[i - 1] == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
            count += 1
            flowerbed[i] = 1
    print('flowebed', flowerbed)
    if count >= n:
        return True
    else:
        return False


def reverse_vowels_of_a_string(s):
    """
    Given a string s, reverse only all the vowels in the string and return it.

    The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

    Example 1:
    -----------
    Input: s = "hello"
    Output: "holle"

    Example 2:
    -----------
    Input: s = "leetcode"
    Output: "leotcede"

    Constraints:
    ------------
    1 <= s.length <= 3 * 105
    s consist of printable ASCII characters.
    """
    vowels = 'aeiouAEIOU'
    given = list(s)
    left, right = 0, len(s) - 1

    while left < right:
        if given[left] in vowels and given[right] in vowels:
            given[left], given[right] = given[right], given[left]
            left += 1
            right -= 1
        elif given[right] not in vowels:
            right -= 1
        elif given[left] not in vowels:
            left += 1
    return ''.join(given)


def reverse_words_in_a_string_151(s):
    """Given an input string s, reverse the order of the words.

    A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

    Return a string of the words in reverse order concatenated by a single space.

    Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

    Example 1:
    ----------
    Input: s = "the sky is blue"
    Output: "blue is sky the"

    Example 2:
    -----------
    Input: s = "  hello world  "
    Output: "world hello"
    Explanation: Your reversed string should not contain leading or trailing spaces.

    Example 3:
    -----------
    Input: s = "a good   example"
    Output: "example good a"
    Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.

    Constraints:
    ------------
    1 <= s.length <= 104
    s contains English letters (upper-case and lower-case), digits, and spaces ' '.
    There is at least one word in s.
    """
    revv = s.split(' ')[::-1]
    return ' '.join([i.strip() for i in revv if i not in (' ')])

def product_of_array_except_self_238(nums):
    """Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

    You must write an algorithm that runs in O(n) time and without using the division operation.

    Example 1:
    ---------
    Input: nums = [1,2,3,4]
    Output: [24,12,8,6]

    Example 2:
    -----------
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

def increasing_triplet_subsequence_334(nums):
    """
    Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

    Example 1:
    -----------
    Input: nums = [1,2,3,4,5]
    Output: true
    Explanation: Any triplet where i < j < k is valid.

    Example 2:
    -----------
    Input: nums = [5,4,3,2,1]
    Output: false
    Explanation: No triplet exists.

    Example 3:
    ----------
    Input: nums = [2,1,5,0,4,6]
    Output: true
    Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.

    Constraints:
    -------------
    1 <= nums.length <= 5 * 105
    -231 <= nums[i] <= 231 - 1"""

    if len(nums) < 3:
        return False

    first, second = float('inf'), float('inf')

    for i in nums:
        if i <= first:
            first = i
        elif i <= second:
            second = i
        else:
            return True

    return False


def string_compression_443(chars):
    """Given an array of characters chars, compress it using the following algorithm:

    Begin with an empty string s. For each group of consecutive repeating characters in chars:

    If the group's length is 1, append the character to s.
    Otherwise, append the character followed by the group's length.
    The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

    After you are done modifying the input array, return the new length of the array.

    You must write an algorithm that uses only constant extra space.

    Example 1:
    ---------
    Input: chars = ["a","a","b","b","c","c","c"]
    Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
    Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".

    Example 2:
    ----------
    Input: chars = ["a"]
    Output: Return 1, and the first character of the input array should be: ["a"]
    Explanation: The only group is "a", which remains uncompressed since it's a single character.

    Example 3:
    -----------
    Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
    Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
    Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".

    Constraints:
    ------------
    1 <= chars.length <= 2000
    chars[i] is a lowercase English letter, uppercase English letter, digit, or symbol."""
    if not chars: return 0
    final = ''
    old = ''
    count = 0
    for i in chars:
        if not old: old = i

        if i == old:
            count += 1
        else:
            if count == 1:
                final += old
            else:
                final += old + str(count)
            old = i
            count = 1

    if count == 1:
        final += old
    else:
        final += old + str(count)

    for i in range(len(final)):
        chars[i] = final[i]

    return len(final)


def find_pairs_with_given_specific_difference(arr, k):
    """Pairs with Specific Difference
    Given an array arr of distinct integers and a nonnegative integer k, write a function findPairsWithGivenDifference that returns an array of all pairs [x,y] in arr, such that x - y = k. If no such pairs exist, return an empty array.

    Note: the order of the pairs in the output array should maintain the order of the y element in the original array.

    Examples:
    ---------
    input:  arr = [0, -1, -2, 2, 1], k = 1
    output: [[1, 0], [0, -1], [-1, -2], [2, 1]]

    input:  arr = [1, 7, 5, 3, 32, 17, 12], k = 17
    output: []

    Constraints:
    ------------
    [time limit] 5000ms
    [input] array.integer arr
    0 ≤ arr.length ≤ 100
    [input]integer k
    k ≥ 0
    [output] array.array.integer"""

    output={}
    res = []

    for x in arr:
        output.update({x-k:x})
    for y in arr:
        if y in output:
            res += [[output[y], y]]

    return res

def decrypt_message(word):
    """Decrypt Message
    An infamous gang of cyber criminals named “The Gray Cyber Mob”, which is behind many hacking attacks and drug trafficking, has recently become a target for the FBI. After intercepting some of their messages, which looked like complete nonsense, the agency learned that they indeed encrypt their messages, and studied their method of encryption.
    Their messages consist of lowercase latin letters only, and every word is encrypted separately as follows:
    Convert every letter to its ASCII value. Add 1 to the first letter, and then for every letter from the second one to the last one, add the value of the previous letter. Subtract 26 from every letter until it is in the range of lowercase letters a-z in ASCII. Convert the values back to letters.

    For instance, to encrypt the word “crime”

    Decrypted message:	c	r	i	m	e
    Step 1:	99	114	105	109	101
    Step 2:	100	214	319	428	529
    Step 3:	100	110	111	116	113
    Encrypted message:	d	n	o	t	q
    The FBI needs an efficient method to decrypt messages. Write a function named decrypt(word) that receives a string that consists of small latin letters only, and returns the decrypted word.

    Explain your solution and analyze its time and space complexities.

    Examples:
    ----------------
    input:  word = "dnotq"
    output: "crime"

    input:  word = "flgxswdliefy"
    output: "encyclopedia"
    Since the function should be used on messages with many words, make sure the function is as efficient as possible in both time and space. Explain the correctness of your function, and analyze its asymptotic runtime and space complexity.

    Note: Most programing languages have built-in methods of converting letters to ASCII values and vica versa. You may search the internet for the appropriate method.

    Constraints:
    --------------
    [time limit] 5000ms
    [input] string word
    The ASCII value of every char is in the range of lowercase letters a-z.
    [output] string"""

    lastval = 1
    final = ""

    for i in range(len(word)):
        currval = ord(word[i]) - lastval

        while (currval < ord('a')):
            currval += 26

        final += chr(currval)
        lastval += currval

    return final