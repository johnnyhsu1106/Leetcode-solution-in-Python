'''
Write a function that takes an unsigned integer and
returns the number of ’1' bits it has (also known as the Hamming weight).

For example, the 32-bit integer ’11' has binary representation 00000000000000000000000000001011,
so the function should return 3.
'''
class Solution:
    def hammingWeight_1(self, n):
        """
        :type n: int
        :rtype: int
        """
        '''
        transfer the integer (10 base) to binary (2 base)
        for example:
            10 -> [0,1,0,1,0,......]
            list bit, i = 0, is constant for 2 ** 0
            list bit, i = 1, is constant for 2 ** 1
            list bit, for given i, element is the constant of 2 ** i


        '''
        bit = [0] * 32
        i = 0
        output = 0
        while n > 0 and i < 32:
            bit[i] = n % 2
            n = n // 2
            output += bit[i]
            i += 1
        return output

    def hammingWeight_2(self,n):
        result = 0
        while n:
            n &= n - 1
            result += 1
        return result

# def main():
#     s = Solution()
#     print(s.hammingWeight(9))
#
#
# if __name__ == '__main__':
#     main()
