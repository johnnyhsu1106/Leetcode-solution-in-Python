'''
Given a string which consists of lowercase or uppercase letters,
find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
'''

from collections import defaultdict
class Solution:
    def longestPalindrome_1(self, s):
        """
        :type s: str
        :rtype: int
        """
        '''
        idea:
        The length of longest palindrome should be 2 * pair of char + single char * 1

        1. Use the dictionary to count all char in s. {char: count}
        2. if any count >= 2, result += count // 2 * 2
        3. if any count is odd, result += 1, the break the loop
        '''
        result = 0
        char_count = defaultdict(int)

        for char in s:
            char_count[char] += 1

        for char in char_count:
            if char_count[char] >= 2:
                result += char_count[char] // 2 * 2

        for char in char_count:
            if char_count[char] % 2 == 1:
                result += 1
                break

        return result


    def longestPalindrome_2(self, s):
        non_pair = set()
        for char in s:
            if char in non_pair:
                non_pair.discard(char)
            else:
                non_pair.add(char)

        non_pair_count = len(non_pair)
        if non_pair_count > 0:
            non_pair_count -= 1

        return len(s) - non_pair_count


# def main():
#     s = Solution()
#     print(s.longestPalindrome_2('ccd'))
#     print(s.longestPalindrome_2('abccccdd'))

# if __name__ == '__main__':
#     main()
