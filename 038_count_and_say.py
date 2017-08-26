'''
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

Example 1:
Input: 1
Output: "1"

Example 2:
Input: 4
Output: "1211"
'''
class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        '''
        idea:
        the whole idea is to get the current value by computing the previous value
        if n = 5 , return '111221'
        so n = 6, '312211'
        then n = 7, '13112221'
        ...
        algorithm:
        count the number of digit and concatate the count and digt into a string
        '''

        s = '1' # initial value
        for i in range(n-1):
            s = self.getNext(s)
        return s

    def getNext(self, s):
        '''
        for example s =  '111221'
        idea:
        like the build-in function: split, split function will split the word by delimiter.
        This is how split(s, delimiter) is implemented.

        def split(string, delimiter=' '):
            word_lst = []
            i = 0
            while i < len(string):
                if string[i] != delimiter:
                    word_start = i
                    while i < len(string) and string[i] != delimiter:
                        i += 1
                    word_lst.append(string[word_start:i])
                i += 1
            return word_lst

        '''
        i = 0
        output = ''
        while i < len(s):
            count = 1 #at least 1 digit
            # count number of same digit
            while i < len(s) - 1 and s[i] == s[i+1]:
                count += 1
                i += 1
            output += str(count) + s[i]
            i += 1 # move to next digit
        return output



# def main():
#     s = Solution()
#     print(s.getNext('1'))
#     print(s.getNext('11'))
#     print(s.getNext('21'))
#
#
# if __name__ == '__main__':
#     main()
