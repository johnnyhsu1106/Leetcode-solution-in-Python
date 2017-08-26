'''
Implement strStr().
Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
'''

class Solution:
    def strStr_1(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        '''
        idea:
        It wants us to implement the build-in funtion str.find()

        Description of str.find()
            It determines if string str occurs in string, or in a substring of string
            if starting index beg and ending index end are given.

            Syntax
            str.find(str, beg=0, end=len(string))
            Parameters
            str -- This specifies the string to be searched.

            beg -- This is the starting index, by default its 0.

            end -- This is the ending index, by default its equal to the length of the string.

            Return Value
            Index if found and -1 otherwise.

        '''
        return haystack.find(needle)



    def strStr_2(self, haystack, needle):
        if haystack == '' and needle == '':
            return 0

        i = 0
        length_h = len(haystack)
        length_n = len(needle)
        while i < (length_h - length_n) + 1:
            if haystack[i:i+length_n] == needle:
                return i
            i += 1
        return -1


# def main():
#
#     s = Solution()
#
#     print(s.strStr_2('hello', 'el'))


# if __name__ == '__main__':
#     main()
