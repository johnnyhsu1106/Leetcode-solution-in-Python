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

class Solution(object):
    def canPermutePalindrome_1(self, s):

        """
        :type s: str
        :rtype: bool
        """
        return sum(v % 2 for v in collections.Counter(s).values()) <  2

    def canPermutePalindrome_2(self, s):

        char_count = {}
        for char in s:
            if char not in char_count:
                char_count[char] = 0
            char_count[char] += 1

        total = 0
        for char in char_count:
            total += char_count[char] % 2
        return total < 2
