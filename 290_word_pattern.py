'''
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match,
such that there is a bijection between a letter in pattern and a non-empty word in str.

Examples:
pattern = "abba", str = "dog cat cat dog" should return true.
pattern = "abba", str = "dog cat cat fish" should return false.
pattern = "aaaa", str = "dog cat cat dog" should return false.
pattern = "abba", str = "dog dog dog dog" should return false.

Notes:
You may assume pattern contains only lowercase letters,
and str contains lowercase letters separated by a single space.
'''
class Solution:
    def wordPattern(self, pattern, string):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """

        '''
        idea:
        using two hashtable to build the exclusive mapping between pattern and string
        only the following situation, this method should return False
        1. word matchs wrong pattern and word is seen before
        2. word matchs wrong pattern and word is never seeen before.

        '''
        words = string.split()
        # edge case
        if len(pattern) != len(words):
            return False


        pattern_map = {}    # key: value = letter: word
        word_map = {}       # key: value = word: letter
        for i in range(len(pattern)):
            letter = pattern[i]
            word = words[i]

            if letter not in pattern_map and word not in word_map:
                pattern_map[letter] = word
                word_map[word] = letter
            elif word not in word_map or word_map[word] != letter:
                #(letter in pattern_map and word not in word_map)
                # (lettern in pattern_map and word_map[word] != letter)
                    return False
        return True
