'''
Given a string s consists of upper/lower-case alphabets and empty space characters ' ',
return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

For example,
Given s = "Hello World",
return 5.
'''
class Solution:
    def lengthOfLastWord_1(self, s):
        """
        :type s: str
        :rtype: int
        """
        '''

        '''
        s_lst = s.strip().split(' ')
        return len(s_lst[-1])

    def lengthOfLastWord_2(self, s):
        '''
        implement the strip() and split() function from the scratch.
        '''
        s_lst = self.split(self.strip(s), ' ')
        return len(s_lst[-1])

    def split(self, s, delimiter=' '):
        output = []
        i = 0
        while i < len(s):
            if s[i] != delimiter:
                start = i
            while i < len(s) and s[i] != delimiter :
                i += 1
            output.append(s[start:i])

            i += 1
        return output


    def strip(self, s, chars=' '):
        '''
        returns a copy of the string
        in which all chars have been stripped from the beginning and the end of the string
        (default whitespace characters).
        '''

        i = 0
        j = len(s)-1
        while i < len(s):
            if s[i] != chars:
                break
            i += 1

        while j >= 0:
            if s[j] != chars:
                break
            j -= 1

        if s[i:j+1] == '':
            return ' '
        return s[i:j+1]

#
# def main():
#     s = Solution()
#
#
#     print(s.lengthOfLastWord_1('a '))
#     print(s.lengthOfLastWord_2('a '))
#
# if __name__ == '__main__':
#     main()
