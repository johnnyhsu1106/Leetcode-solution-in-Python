'''
Given an integer n, return the number of trailing zeroes in n!.
Note: Your solution should be in logarithmic time complexity.
For example:
4! = 24,   return 0
5! = 120 , return 1
10! = 10*9*8.....*1, return 2
25! = 25*...*20..*15..*10..*5...*1,  return 6 
'''
class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        '''
        idea:
        count how many 5 exists in n factorial

        '''
        output = 0
        while n > 0:
            output += n // 5
            n = n // 5
        return output

# def main():
#     s = Solution()
#     print(s.trailingZeroes(5))
#     print(s.trailingZeroes(10))
#
#
# if __name__ == '__main__':
#     main()
