'''
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction
(ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
Example 2:
Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.
'''

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        '''
        The profit = current price - min price shown before
        use for loop to calculate the profit for each price
        if at this point, the profit is greater than before, it would/ may be the max profit.
        '''


        max_profit = 0
        min_price = float('inf')
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(price - min_price, max_profit)
        return max_profit


        # old fashion way ---faster because not calling min and max function
        # max_profit = 0
        # min_price = float('inf')
        # for price in prices:
        #     if price <= min_price:
        #         min_price = price
        #     profit = price - min_price
        #     if profit >= max_profit:
        #         max_profit = profit
        # return max_profit



# ================= Test Area ==================
# def main():
#     s = Solution()
#     print(s.maxProfit([7, 1, 5, 3, 6, 4]))
#     print(s.maxProfit([7, 6, 4, 3, 1]))
#
# if __name__ == '__main__':
#     main()
