'''
Given an integer, write a function to determine if it is a power of two.
'''

class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        #  edge case: n <=0 , return False
        if n <= 0:
            return False

        #  sepcial case (edge case): 2 ** 1 = 0
        if n == 1:
            return True
        #  if not power of 2, it would be a multiply of 2 and odd number
        while n > 1:
            if n % 2 == 1: # odd number
                return False
            n = n // 2
        return True

# def main():
#     s = Solution()
#     print(s.isPowerOfTwo(-1) == False)
#     print(s.isPowerOfTwo(0) == False)
#     print(s.isPowerOfTwo(1) == True)
#     print(s.isPowerOfTwo(2) == True)
#     print(s.isPowerOfTwo(8) == True)
#     print(s.isPowerOfTwo(9) == False)
#     print(s.isPowerOfTwo(10) == False)
#
#
# if __name__ == '__main__':
#     main()
