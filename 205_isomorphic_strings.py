'''
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters.
No two characters may map to the same character but a character may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.

Note:
You may assume both s and t have the same length.
'''
class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        s2t_map = {} # key: value = char in s : char in t
        t2s_map = {} # key: value = char in t : char in s
        for charS, charT in zip(s,t):
            if charS not in s2t_map and charT not in t2s_map:
                s2t_map[charS] = charT
                t2s_map[charT] = charS
            elif charT not in t2s_map or t2s_map[charT] !=  charS :
                return False
        return True



# def main():
#     solution = Solution()
#     s = 'egg'
#     t = 'add'
#     print(solution.isIsomorphic(s,t))
#     s = 'foo'
#     t = 'bar'
#     print(solution.isIsomorphic(s,t))
#     s = 'paper'
#     t = 'title'
#     print(solution.isIsomorphic(s,t))
#
# if __name__ == '__main__':
#     main()
