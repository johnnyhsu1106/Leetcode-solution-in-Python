'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.
'''

class Solution:



    def isPalindrome_1(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # edge case: s = '', return True
        if len(s) == 0:
            return True

        s = s.lower()
        s_char = ''
        for char in s:
            if char.isalnum():
                s_char += char

        for i in range(len(s_char)//2):
            if s_char[i] != s_char[len(s_char) -i - 1 ]:
                return False
        return True



    def isPalindrome_2(self, s):
        '''
         a better way
         idea: from the beingng of the string and the end of the string.
         fidn the chars are both strings by usuing str.isalnum()
         then lower the chars and compare they are equal no not.
         the codition is i < j , keep find the i and j, which s[i] and s[j] are both either alphabets or numbers
         i is the index from the begining of string
         j is the index from the end of string
        '''
        i = 0
        j = len(s) -1
        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1

            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True

# 
# def main():
#     s = Solution()
#     print(s.isPalindrome_1("0P"))
#     print(s.isPalindrome_1("A man, a plan, a canal: Panama"))
#
#     print(s.isPalindrome_2("0P"))
#     print(s.isPalindrome_2("A man, a plan, a canal: Panama"))
#
#
# if __name__ == '__main__':
#     main()
