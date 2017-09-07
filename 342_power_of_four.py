'''
 Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example:
Given num = 16, return true. Given num = 5, return false.

Follow up: Could you solve it without loops/recursion?
'''

class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        '''

        '''
        # edge case: the following cases are edge cases.
        # zero or negative number
        if num <= 0:
            return False
        #  4 ** 0 = 1
        elif num == 1:
            return True
        #  odd number
        elif num % 2 == 1:
            return False



        while num >= 4:
            if num % 4 != 0:
                return False
            num = num // 4
        return num == 1
