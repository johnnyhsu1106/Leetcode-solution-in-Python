'''
You are given coins of different denominations and a total amount of money.
Write a function to compute the number of combinations that make up that amount.
You may assume that you have infinite number of each kind of coin.

Note: You can assume that

0 <= amount <= 5000
1 <= coin <= 5000
the number of coins is less than 500
the answer is guaranteed to fit into signed 32-bit integer

Example 1:
Input: amount = 5, coins = [1, 2, 5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1

Example 2:
Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.

Example 3:
Input: amount = 10, coins = [10]
Output: 1
'''

class Solution:
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """


        memo = {}
        index = 0
        return self.change_helper(amount, coins, index, memo)



    def change_helper(self, amount, coins, index, memo):


        #  base case
        if amount == 0:
            return 1

        if index >= len(coins):
            return 0


        #  memorization
        key = str(amount) + '-' + str(index)
        if key in memo:
            return memo[key]
        # memo[key] = 0
        amount_with_coin = 0
        output = 0

        while amount_with_coin <= amount:
            remain_amount = amount - amount_with_coin
            output += self.change_helper(remain_amount, coins, index + 1, memo)
            amount_with_coin += coins[index]

        memo[key] = output

        return output

# def main():
#     s = Solution()
#     print(s.change(5, [1,2,5]))
#     print(s.change(3, [2]))
#     print(s.change(10, [10]))
#
#
#
# if __name__ == '__main__':
#     main()
