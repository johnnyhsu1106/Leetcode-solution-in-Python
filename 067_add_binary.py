'''
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".

'''
class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        '''
        '''
        if len(a) >= len(b):
            big = a
            small = b
        else:
            big = b
            small = a

        n = len(small)

        output = ''
        carry = 0
        for i in range(n-1, -1, -1):
            sum_binary = int(big[i+len(big)-len(a)]) + int(small[i]) + carry
            if sum_binary > 1:
                sum_binary = sum_binary % 2
                carry = 1
            else:
                carry = 0
            output = str(sum_binary) + output


        if len(a) != len(b):
            for i in range(len(big)-n-1, -1, -1):
                sum_binary = int(big[i]) + carry
                if sum_binary > 1:
                    sum_binary %= sum_binary
                    carry = 1
                else:
                    carry = 0
                output = str(sum_binary) + output

        if carry == 1:
            output = str(1) + output

        return output


# def main():
#     s = Solution()
#     print(s.addBinary('11', '1'))
#     print(s.addBinary('101', '011') )
#     print(s.addBinary('1010', '1011'))
#     print(s.addBinary('1111', '1111'))
#     print(s.addBinary('100', '110010'))
#
#
#
# if __name__ == '__main__':
#     main()
