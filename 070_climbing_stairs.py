'''
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.
'''

result_dict = {}

class Solution:
    def climbStairs_1(self, n):
        """
        :type n: int
        :rtype: int
        """
        '''
        n = 1, result(1) = 1 , (1)
        n = 2, result(2) = 1 + 1 = 2 , (1,1) or (2)
        n = 3, result(3) = 1 + 2 = 3, (1,1,1), (1,2), (2,1), which is result(1) + result(2)
        n = 4, result(4) = 2 + 3 = 5, (1,1,1,1), (1,2,1), (1,1,2) ,(2,1,1),(2,2), which is result(2) + result(3)
        n = 5, result(5) = 3 + 5 = 8,
        '''
        if n == 1:
            return 1
        if n == 2:
            return 2

        if n not in result_dict:
            result_dict[n] = self.climbStairs_1(n-1) + self.climbStairs_1(n-2)
        return result_dict[n]


    def climbStairs_2(self, n):
        previous, current = 0, 1
        for i in range(n):
            previous, current = current, previous + current
        return current


# def main():
#     s = Solution()
#     print(s.climbStairs_1(10))
#     print(s.climbStairs_2(10))
#
#
# if __name__ == '__main__':
#     main()
