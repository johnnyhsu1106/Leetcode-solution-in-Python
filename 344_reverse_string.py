'''
Write a function that takes a string as input and returns the string reversed.
Example:
Given s = "hello", return "olleh".
'''
class Solution:
    def reverseString_1(self, s):
        '''
        use the for loop to concatenate the char backwardly.
        '''
        output = ''
        n = len(s)
        for i in range(n):
            output += s[n-1-i]
        return output

    def reverseString_2(self, s):
        '''
        use the recursive method and string slicing to reverse string
        '''
        if len(s) == 1:
            return s
        return s[-1] + self.reverseString_2(s[0:-1])


    def reverseString_3(self, s):
        '''
        '''

        n = len(s)
        s_lst = list(s)
        for i in range(n//2):
            temp = s_lst[i]
            s_lst[i] = s_lst[n-i-1]
            s_lst[n-i-1] = temp
        return ''.join(s_lst)



    def reverseString_4(self, s):

        n = len(s)
        if n % 2 == 1:
            output = s[n//2]
            for i in range(n//2):
                output = s[n//2 + i + 1] + output + s[n//2 - i - 1]
            return output
        else:
            output = ''
            for i in range(n//2):
                output = s[n//2 + i ] + output + s[n//2 -i -1]
            return output

    def reverseString_5(self, s):
        return s[::-1]

    def reverseString_6(self, s):

        i, j  = 0, len(s)-1
        string = list(s)

        while i < j:
            string[i], string[j] = string[j], string[i]
            i += 1
            j += 1
        return ''.join(string)

# def main():
#     solution = Solution()
#     print(solution.reverseString_1('hello'))
#     print(solution.reverseString_2('hello'))
#     print(solution.reverseString_3('hello'))
#     print(solution.reverseString_4('hello'))
#
#
# if __name__ == '__main__':
#     main()
