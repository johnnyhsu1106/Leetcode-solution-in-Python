'''
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process:
Starting with any positive integer, replace the number by the sum of the squares of its digits,
and repeat the process until the number equals 1 (where it will stay), or
it loops endlessly in a cycle which does not include 1.

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
        num_dict = {} # a storage to store all number if number appears before
        # in order to avoid infinite loop, use a dict, set, or list to storage the number, which apprear before.
        # For Example
        # compute is 4 happy number
        # 4 -> 16 -> 37 -> 57 -> 64 -> 42 -> 20 -> 4.......the following precess will repeat infinitely

        while n != 1 and n not in num_dict:
            num_dict[n] = n
            output = 0
            for digit in str(n):
                output += int(digit) ** 2
            n = int(output)
        return n == 1



# =================== Testing area ===================
# def main():
#     s = Solution()
#     print(s.isHappy(7))


# if __name__ == '__main__':
#     main()
