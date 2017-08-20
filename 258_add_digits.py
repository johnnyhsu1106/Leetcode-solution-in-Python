'''
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.
For example:
Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.
Follow up:
Could you do it without any loop/recursion in O(1) runtime?
'''

class Solution:
    def addDigits_1(self, num):
        """
        :type num: int
        :rtype: int
        """
        '''
        for exampl; num = 1348
        then 1348 -> '1348' -> ['1','3','4','8']
        summation of ['1','3','4','8']
        '16' -> ['1','6']
        repeat this process, until only one element in the list
        '''
        num_lst = list(str(num))
        while len(num_lst) > 1:
            total = 0
            for num in num_lst:
                total += int(num)

            num_lst = list(str(total))
        return int(num_lst[0])


    def addDigits_2(self, num):
        while num > 10:
            n = num
            total = 0
            while n // 10 > 0:
                total += n % 10
                n = n // 10
            num = n % 10 + total
        return num


    def addDigits_3(self, num):
        if num % 9 == 0:
            return 9
        return num % 9



# def main():
#     s = Solution()
#
#     print(s.addDigits_1(148))
#     print(s.addDigits_2(148))
#     print(s.addDigits_3(148))
#
#
# if __name__ == '__main__':
#     main()
