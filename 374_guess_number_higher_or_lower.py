
'''
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number is higher or lower.

You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):

-1 : My number is lower
 1 : My number is higher
 0 : Congrats! You got it!
Example:
n = 10, I pick 6.

Return 6.
'''
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):



class Solution:
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        '''
        A typical binary search question.
        There are two way to solve this question.
        1. use recursive method
        2. use iterative method as follow.

        '''
        first = 1
        last = n


        while True:
            middle = first + (last - first) // 2
            feedback = guess(middle)
            if feedback == 0:
                break
            elif feedback == 1:
                first = middle + 1
            else:
                last = middle -1

        return middle
