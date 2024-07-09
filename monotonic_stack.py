def daily_temperatures_739(temperatures):
    #monotonic increasing
    """Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

    Example 1:
    ----------
    Input: temperatures = [73,74,75,71,69,72,76,73]
    Output: [1,1,4,2,1,1,0,0]

    Example 2:
    ----------
    Input: temperatures = [30,40,50,60]
    Output: [1,1,1,0]

    Example 3:
    ----------
    Input: temperatures = [30,60,90]
    Output: [1,1,0]


    Constraints:
    ------------
    1 <= temperatures.length <= 105
    30 <= temperatures[i] <= 100"""

    stack = []
    res = [0] * len(temperatures)

    for i, temp in enumerate(temperatures):

        while stack and temperatures[stack[-1]] < temp:
            index = stack.pop()
            res[index] = i - index
        stack.append(i)  # storing indexes

    return res


    #for monotonic decreasing stack
    a = [100, 80, 60, 70, 60, 75, 85]
    s = []
    res = [1] * len(a)
    for i, val in enumerate(a):

        while s and a[s[-1]] < val:
            index = s.pop()
            res[i] += res[index]
        s.append(i)
    return res
    #res = [1, 1, 1, 2, 1, 4, 6]
