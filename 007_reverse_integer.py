'''
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

click to show spoilers.

Have you thought about this?
Here are some good questions to ask before coding.
Bonus points for you if you have already thought through this!

If the integer's last digit is 0, what should the output be? ie, cases such as 10, 100.

Did you notice that the reversed integer might overflow?
Assume the input is a 32-bit integer, then the reverse of 1000000003 overflows.
How should you handle such cases?

For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

Note:
The input is assumed to be a 32-bit signed integer. Your function should return 0 when the reversed integer overflows.
'''

class Solution:
    def reverse_1(self, x):
        """
        :type x: int
        :rtype: int
        """
        '''
        idea: brute force - convert integer to string, then to list
        cons: cost extra space
        check the output, if output overflows, return 0
        '''
        # edge case
        if x >= 0 and x < 10:
            return x

        output = 0
        x = list(str(x))
        x = x[::-1] #reverse the list

        if x[-1] == '-':
            sign = x[-1]
            i = 0
            while x[i] == 0:
                i += 1
            output = int(''.join([x[-1]] + x[i:-1]))
        else:
            i = 0
            while x[i] == 0:
                i += 1
            output = int(''.join(x[i:]))

        if output > 2**31 -1 or output < - 2**31:
            return 0
        return output



    def reverse_2(self, x):
        '''
        a better version of reverse_1: convert integer to string
        '''
        if x < 0:
            output = int(str(x)[::-1][-1] + str(x)[::-1][:-1])
        else:
            output = int(str(x)[::-1])

        if output > 2**31 -1 or output < - 2**31:
            return 0
        return output




    def reverse_3(self, x):
        '''
        idea:
        create a method to reverse positive integer called reversePositiveInteger()

        '''
        # edge case
        if x >= 0 and x < 10:
            return x

        if x > 0:
            output = self._reversePositiveInteger(x)

        else:
            x = - x
            output = self._reversePositiveInteger(x)
            output = -output

        #  check if output overflows
        if output > 2**31 -1 or output < - 2**31:
            return 0
        return output


    def _reversePositiveInteger(self, x):
        '''
        This method only reverse positive integer
        1. Get the last digit by mod 10, add it to output
        2. Then, output multiply 10,
        3. Finally, update x by dividing 10 until x == 0, then stop

        For example:
        x = 123, output = 0

        loop 1:
        digit = 123 % 10 = 3, output = (0 * 10 + 3)  = 3, x = 123 // 10 = 12

        loop 2:
        digit = 12 % 10 = 2, output = (3 * 10 + 2)  = 32, x = 12 // 10 = 1

        loop 2:
        digit = 1 % 10 = 1, output = (32 * 10  + 1) * 10 = 321, x = 1 // 10 = 0

        return output


        '''
        output = 0
        while x > 0:
            digit = x % 10
            output = (output * 10 + digit)
            x = x // 10
        return output


# def main():
#     s = Solution()

    # print(s.reverse_1(0) == 0)
    # print(s.reverse_1(123) == 321)
    # print(s.reverse_1(-123) == -321)


    # print(s.reverse_2(0) == 0)
    # print(s.reverse_2(123) == 321)
    # print(s.reverse_2(-123) == -321)


    # print(s.reverse_3(0) == 0)
    # print(s.reverse_3(123) == 321)
    # print(s.reverse_3(-123) == -321)
    #
    #

#
# if __name__ == '__main__':
#     main()
