'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
(you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
'''

class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        # the relationship of numRows and step
        step = 2 * numRows - 2
        result = ''
        for i in range(numRows):
            for j in range(i,len(s), step):
                result += s[j]
                #  not the first row and last row.
                #
                if (i > 0 and i < numRows-1) and j + step - 2 * i < len(s):
                    result += s[j+step-2*i]
        return result
