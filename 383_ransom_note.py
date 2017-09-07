'''
Given an arbitrary ransom note string and another string containing letters from all the magazines,
write a function that will return true if the ransom note can be constructed from the magazines ;
otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
'''
class Solution:
    def canConstruct_1(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        '''
        idea:
        brute force - use two dictionary/map to count the number of letter in ransomNote and magazine
        '''
        ransom_map = {}
        magazine_map = {}
        for letter in ransomNote:
            if letter not in ransom_map:
                ransom_map[letter] = 0
            ransom_map[letter] += 1

        for letter in magazine:
            if letter not in magazine_map:
                magazine_map[letter] = 0
            magazine_map[letter] += 1

        for letter in ransom_map:
            if letter not in magazine_map:
                return False
            else:
                if ransom_map[letter] > magazine_map[letter]:
                    return False
        return True



    def canConstruct_2(self, ransomNote, magazine):
        '''
        idea:
        Use the list/array, whose length is 26, to store the number of letter in each corresponding position.
        '''
        ramson_count = [0] * 26
        magazine_count = [0] * 26
        for char in ransomNote:
            position = ord(char) - ord('a')
            ramson_count[position] += 1

        for char in magazine:
            position = ord(char) - ord('a')
            magazine_count[position] += 1

        for i in range(len(ramson_count)):
            if ramson_count[i] > magazine_count[i]:
                return False
        return True

#
#
# def main():
#     s = Solution()
#     print(s.canConstruct_1("a", "b"))
#     print(s.canConstruct_1("aa", "ab"))
#     print(s.canConstruct_1("aa", "aab"))
#
#
# if __name__ == '__main__':
#     main()
