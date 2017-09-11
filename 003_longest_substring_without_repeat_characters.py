'''
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.
Given "bbbbb", the answer is "b", with the length of 1.
Given "pwwkew", the answer is "wke", with the length of 3.
Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''
from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring_1(self, s):
        """
        :type s: str
        :rtype: int
        """
        '''
        idea:
        Use two pointers, start, last, to solve this problem.

        '''
        result = 0
        lookup = defaultdict(int) # a dictionary to track char showed up.

        last = 0
        for start in range(len(s)):
            while last < len(s) and lookup[s[last]]== 0:
                lookup[s[last]] = 1
                result = max(result, last - start + 1)
                last += 1
            lookup[s[start]] = 0
        return result


    def lengthOfLongestSubstring_2(self, s):
        '''
        idea:
        '''

        result = 0
        left = 0        # a pointer to track the each valid substring's starting point
        lookup = {}     # a dictionary/lookup to track the char and its position, key:value = char:index
        for i in range(len(s)):
            if s[i] in lookup and lookup[s[i]] >= left:
                left = lookup[s[i]] + 1

            lookup[s[i]] = i
            result = max(result, i - left + 1)
        return result



# def main():
#
# if __name__ == '__main__':
#     main()
