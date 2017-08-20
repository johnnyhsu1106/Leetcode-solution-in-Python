'''
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters?
How would you adapt your solution to such case?
'''
class Solution:
    def isAnagram_1(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        #  edge case

        if len(t) != len(s):
            return False
        return sorted(s) == sorted(t)

    def isAnagram_2(self, s, t):

        if len(t) != len(s):
            return False

        char_dict = {}
        for char in s:
            if char not in char_dict:
                char_dict[char] = 0
            char_dict[char] += 1

        for char in t:
            if char not in char_dict:
                return False
            char_dict[char] -= 1

        for char in char_dict:
            if char_dict[char] != 0:
                return False
        return True


    def isAnagram_3(self, s, t):
        if len(s) != len(t):
            return False
        count = collections.defaultdict(int)
        for c in s:
            count[c] += 1
        for c in t:
            count[c] -= 1
            if count[c] < 0:
                return False
        return True
