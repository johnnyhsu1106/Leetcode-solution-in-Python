'''
Reverse bits of a given 32 bits unsigned integer.

For example, given input 43261596 (represented in binary as 00000010100101000001111010011100),
return 964176192 (represented in binary as 00111001011110000010100101000000).

Follow up:
If this function is called many times, how would you optimize it?

Related problem: Reverse Integer
'''

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        '''
        idea: modularize each step.
        '''

        bits = self.int2binary(n)
        bits.reverse()
        result = self.binary2int(bits)
        return result


    def int2binary(self, n):
        '''
        input: Int
        output: List
        '''
        output = [0] * 32
        i = 31
        while n > 0:
            output[i] = n % 2
            n = n // 2
            i -= 1
        return output


    def binary2int(self, bits):
        '''
        input: List
        output: Int
        '''
        output = 0
        for i in range(len(bits)):
            output += 2 ** (len(bits) -1-i) * int(bits[i])
        return output
