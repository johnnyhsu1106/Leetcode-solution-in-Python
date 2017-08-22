'''
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
'''

class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        '''
        idea:
        consider the following situation:
        read the roman integer from right to left
        1. the roman integer is greater or equal to the one follows it.
           read the one roman integer at one time
            I = 1
            III = 3 = I + I + I = 3
            VI = 6 ＝ V + I = 5 + 1

        2. the roman number is smaller than the one follows it.
            read the two roman integers at one time
            IV = 4 = V - I = 5 - 1
            IX = 9 = X - I = 10 - 1
            XC = 90 = C - X = 100 - 10
        '''

        #  use the map (dictionary) to map the roman integer (key) to integer (value)
        roman_int_map = {'I':1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        output = 0
        for i in range(len(s)):
            num1 = roman_int_map[s[i-1]]
            num2 = roman_int_map[s[i]]

            if i > 0 and  num2 > num1 :
                output += num2 - 2 * num1
            else:
                output += num2

        return output

# def main():
#     s = Solution()
#     print(s.romanToInt('DCXXI') == 621)
#     print(s.romanToInt('MCDLXXVI') == 1476)
#     print(s.romanToInt('MDCLXVI')== 1666)
#     print(s.romanToInt('MCMLXXXIV') == 1984)
#     print(s.romanToInt('MCMXCVI') == 1996)


if __name__ == '__main__':
    main()
