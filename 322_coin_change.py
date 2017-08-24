'''
You are given coins of different denominations and a total amount of money amount.
Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:
coins = [1, 2, 5], amount = 11
return 3 (11 = 5 + 5 + 1)

Example 2:
coins = [2], amount = 3
return -1.

'''

class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        '''
        A solution without memorization and dynamic programming
        '''
        memo = {} # storage for memorization
        return  self.coinChange_helper(coins, amount, memo)

    def coinChange_helper(self, coins, amount , memo):

        #  edeg case:
        if amount in coins:
            memo[amount] = 1
            return 1

        if amount in memo:
            return memo[amount]

        # default output
        min_coins = amount

        valid_coins = [ coin for coin in coins if coin <= amount]

        for coin_value in valid_coins:
            num_coins = 1 + self.coinChange_helper(coins, amount - coin_value, memo)

            if num_coins < min_coins:
                min_coins = num_coins
                memo[amount] = min_coins


        return min_coins


# def main():
#     s = Solution()
#     # print(s.coinChange([2],3))
#     print(s.coinChange([1,2,5],11))
#
# if __name__ == '__main__':
#     main()
