'''
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
'''

class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        '''
        idea: link binary, it carrys every 26.
        please see the problem 171. It is a similiar problem
        '''

        letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        output = ''
        while n > 0:
            digit = (n - 1)% 26
            output =  letters[digit] + output
            n = (n - 1)// 26
        return output

# def main():
#     s = Solution()
#     print(s.convertToTitle(1))
#     print(s.convertToTitle(26))
#     print(s.convertToTitle(28))
#
#
# if __name__ == '__main__':
#     main()
