'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit.
You may complete as many transactions as you like
(ie, buy one and sell one share of the stock multiple times).
However, you may not engage in multiple transactions at the same time
(ie, you must sell the stock before you buy again).
Exapmle 1:
Input: []
Output: 0

Example 2:
Input: [2,1]
Output: 0

Exapmle 3:
Input: [1,2,4]
Output: 3

Example 4:
Input: [1, 5, 3, 6, 4]
Output:  (5-1) + (6-3) = 7
'''

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        i = 0
        while i < len(prices) -1:
            profit += max(0, prices[i+1] - prices[i])
            i += 1
        return profit




# def main():
#     s = Solution()
#     print(s.maxProfit([1,2, 4]))
#
#     print(s.maxProfit([7, 1, 5, 3, 6, 4]))
#
# if __name__ == '__main__':
#     main()
