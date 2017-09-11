'''
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character
while preserving the order of characters.
No two characters may lookup to the same character but a character may lookup to itself.

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
        '''
        idea:
        see the problem 290 as well.
        '''
        # edge case
        if len(s) != len(t):
            return False

        s2t_lookup = {} # key: value = char in s : char in t
        t2s_lookup = {} # key: value = char in t : char in s

        for char_s, char_t in zip(s,t):
            if char_s not in s2t_lookup and char_t not in t2s_lookup:
                s2t_lookup[char_s] = char_t
                t2s_lookup[char_t] = char_s
            elif char_t not in t2s_lookup or t2s_lookup[char_t] !=  char_s:
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
