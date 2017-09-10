'''
Given a string, determine if a permutation of the string could form a palindrome.

For example,
"code" -> False, "aab" -> True, "carerac" -> True.

General Analysis:

This problem is easy.
Basic idea is:
if s with odd characters, only one character is allowed to appear odd times.
if s with even characters, each character should appear even times.
'''
from collections import defaultdict

class Solution:
    def canPermutePalindrome_1(self, s):

        """
        :type s: str
        :rtype: bool
        """
        return sum(v % 2 for v in collections.Counter(s).values()) <  2

    def canPermutePalindrome_2(self, s):

        char_count = defaultdict(int)
        for char in s:
            char_count[char] += 1

        total = 0
        for char in char_count:
            total += char_count[char] % 2
        #  if total = 0 or 1 , it means the permutation of this string may form palindrome
        return total < 2

# def main():
#     s = Solution()
#     print(s.canPermutePalindrome_2('code') == False)
#     print(s.canPermutePalindrome_2('aab') == True)
#     print(s.canPermutePalindrome_2('carerac') == True)
#
#
# if __name__ == '__main__':
#     main()
