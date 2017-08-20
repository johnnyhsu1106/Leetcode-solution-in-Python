'''
Related to question Excel Sheet Column Title

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
'''
class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        output = 0
        for i in range(len(s)):
            digit = ord(s[i]) - ord('A') + 1
            output += digit * 26 ** (len(s) - i - 1)
        return output
