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


def online_stock_span_901():
    """Design an algorithm that collects daily price quotes for some stock and returns the span of that stock's price for the current day.

    The span of the stock's price in one day is the maximum number of consecutive days (starting from that day and going backward) for which the stock price was less than or equal to the price of that day.

    For example, if the prices of the stock in the last four days is [7,2,1,2] and the price of the stock today is 2, then the span of today is 4 because starting from today, the price of the stock was less than or equal 2 for 4 consecutive days.
    Also, if the prices of the stock in the last four days is [7,34,1,2] and the price of the stock today is 8, then the span of today is 3 because starting from today, the price of the stock was less than or equal 8 for 3 consecutive days.
    Implement the StockSpanner class:

    StockSpanner() Initializes the object of the class.
    int next(int price) Returns the span of the stock's price given that today's price is price.


    Example 1:
    -------------
    Input
    ["StockSpanner", "next", "next", "next", "next", "next", "next", "next"]
    [[], [100], [80], [60], [70], [60], [75], [85]]
    Output
    [null, 1, 1, 1, 2, 1, 4, 6]

    Explanation
    -----------
    StockSpanner stockSpanner = new StockSpanner();
    stockSpanner.next(100); // return 1
    stockSpanner.next(80);  // return 1
    stockSpanner.next(60);  // return 1
    stockSpanner.next(70);  // return 2
    stockSpanner.next(60);  // return 1
    stockSpanner.next(75);  // return 4, because the last 4 prices (including today's price of 75) were less than or equal to today's price.
    stockSpanner.next(85);  // return 6


    Constraints:
    ------------
    1 <= price <= 105
    At most 104 calls will be made to next."""

    class StockSpanner:

        def __init__(self):
            self.stack = []

        def next(self, price: int) -> int:
            val = 1
            last_val = 0
            while self.stack and self.stack[-1][0] <= price:
                index, last_val = self.stack.pop()
                val += last_val
            self.stack.append((price, val))
            return val
