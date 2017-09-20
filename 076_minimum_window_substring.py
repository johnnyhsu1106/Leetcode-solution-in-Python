'''
Given a string source and a string target,
find the minimum window in source which will contain all the characters in target.

Notice:
If there is no such window in source that covers all characters in target, return the emtpy string "".
If there are multiple such windows,
you are guaranteed that there will always be only one unique minimum window in source.

For example,
For source = "ADOBECODEBANC", target = "ABC"
Minimum window is "BANC".

'''
from collections import defaultdict
class Solution(object):
    def minWindow_1(self, source, target):
        '''
        @param: source : A string
        @param: target: A string
        @return: A string denote the minimum window, return "" if there is no such a string
        '''
        '''
        idea:
        Use the two pointer - sliding windows and hash table to track the all characters
        '''
        # create a hashmap/dictionary for target, {key: value = char: count}
        s_char_count = defaultdict(int)
        t_char_count = defaultdict(int)

        for char in target:
            t_char_count[char] += 1

        j = 0
        min_substr = ''
        min_length = float('inf')

        for i in range(len(source)):
            while j < len(source) and not self.is_hash_contain(s_char_count, t_char_count):
                s_char_count[source[j]] += 1
                j += 1

            if self.is_contain(s_char_count, t_char_count):
                if min_length > j - i:
                    min_length = j - i
                    min_substr = source[i:j]
            s_char_count[source[i]] -= 1

        return min_substr

    def is_hash_contain(self, s_char_count, t_char_count):
        for char in t_char_count:
            if char not in s_char_count or s_char_count[char] < t_char_count[char]:
                return False
        return True


    def minWindow_2(self, source, target):
        '''
        idea:
        Use the two pointers (sliding windows) and hash table;
        However, choose to use array/list to implment hash table.
        Assume; only english (uppercase /lowercase) characters are included in the string.
        My idea: not recommend to use array/list as hash table
        because the default build-in dictionary is already too good.
        '''
        s_char_count = [0] * 52  # only 26 uppercase and 26 lowercase letters
        t_char_count = [0] * 52  # only 26 uppercase and 26 lowercase letters

        # build t_char_count: each index corresponds to a to z, A to Z. Element are the number of letter
        for char in target:
            idx = self.char_2_index(char)
            t_char_count[idx] += 1

        j = 0
        min_substr = ''
        min_length = float('inf')

        for i in range(len(source)):

            while j < len(source) and not self.is_list_contain(s_char_count, t_char_count):

                idx = self.char_2_index(source[j])
                s_char_count[idx] += 1
                j += 1

            if self.is_list_contain(s_char_count, t_char_count):
                if min_length > j - i:
                    min_length = j - i
                    min_substr = source[i:j]
                idx = self.char_2_index(source[i])
                s_char_count[idx] -= 1

        return min_substr


    def char_2_index(self, char):
        if ord(char) >= ord('a'):
            idx = ord(char) - ord('a') + 26
        else:
            idx = ord(char) - ord('A')
        return idx


    def is_list_contain(self, s_char_count, t_char_count):
        for i in range(len(t_char_count)):
            if s_char_count[i] < t_char_count[i]:
                return False
        return True
