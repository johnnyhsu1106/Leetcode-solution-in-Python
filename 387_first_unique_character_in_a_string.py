'''
Given a string, find the first non-repeating character in it and return it's index.
If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
'''


# from collections import defaultdict

class Solution:
    def firstUniqChar_1(self, s):
        """
        :type s: str
        :rtype: int
        """
        '''
        idea:
        1. Use the hash map/ dictionary to count the number of each char
        2. Find all unique chars if the number of this char is 1.
        3. Go through each char in string, if char exists in unique chars set, return index;
           otherwise, return -1

        Time: O(n)
        '''
        lookup = {}
        for char in s:
            if char not in lookup:
                lookup[char] = 0
            lookup[char] += 1

        unique_chars = set()
        for char in loopup:
            if lookup[char] == 1:
                unique_chars.add(char)

        for i, char in enumerate(s):
            if char in unique_chars:
                return i
        return -1


    def firstUniqChar_2(self, s):
        '''
        idea:
        1. A hash map/ dictionary to store the char and index. key: value = char: index
        2. A set to store all posible unique chars' index
        '''
        lookup = {}
        candidtates = set()
        for i, char in enumerate(s):
            if char in lookup:
                candidtates.discard(lookup[char])
            else:
                # shift the index: all index plus 1
                lookup[char] = i
                candidtates.add(i)

        if len(candidtates) == 0:
            return -1
        return min(candidtates)

        # the line from 65 to 67 is equal to the following syntax
        # return min(candidtates) if candidtates else -1



# def main():
#     s = Solution()
#     print(s.firstUniqChar_1('leetcode'))
#     print(s.firstUniqChar_1('loveleetcode'))
#     print(s.firstUniqChar_2('leetcode'))
#     print(s.firstUniqChar_2('loveleetcode'))
#
# if __name__ == '__main__':
#     main()
