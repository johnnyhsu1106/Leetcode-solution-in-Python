'''
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer,
replace the number by the sum of the squares of its digits,
and repeat the process until the number equals 1 (where it will stay),
or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number

1 ** 2 + 9 ** 2 = 82
8 ** 2 + 2 ** 2 = 68
6 ** 2 + 8 ** 2 = 100
1 ** 2 + 0 ** 2 + 0 ** 2 = 1
'''

class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        '''
        idea:
        Use a dictionary/hash map (lookup) to track the number we calculated.
        The infinite loop may happen if we re-calcualte the same number
        For example:
        4 -> 16 -> 37 -> 58 -> 89 -> 145 -> 42 -> 20 -> 4.....repeat the cycle
        '''
        lookup = {} # track the number we already calculated
        while n != 1 and n not in lookup:
            lookup[n] = n
            n = self.next_number(n)
        return n == 1


    def next_number(self, n):
        output = 0
        for digit in str(n):
            output += int(digit) ** 2
        n = int(output)
        return n

#
# def main():
#     s = Solution()
#     print(s.isHappy(19))
#     print(s.isHappy(4))
#
# if __name__ == '__main__':
#     main()
