'''
Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.
You may assume the integer do not contain any leading zero, except the number 0 itself.
The digits are stored such that the most significant digit is at the head of the list.
'''

class Solution:
    def plusOne_1(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        '''
        idea:
        brute force
        however, this is not a good way and not a
        '''
        digits = [str(digit) for digit in digits]
        digits = int(''.join(digits))
        digits += 1
        return [int(digit) for digit in str(digits)]



    def plusOne_2(self, digits):
        '''
        idea:
        Go through each digit from the end of list
        calcualte the carry and add carry to next element

        '''
        carry = 1
        for i in range(len(digits)-1, -1 , -1):
            digits[i] += carry
            carry = digits[i] // 10
            digits[i] %= 10
        if carry:
            digits.insert(0, carry)
        return digits



# def main():
    # s = Solution()
    # print(s.plusOne_1([0]) == [1])
    # print(s.plusOne_1([9]) == [1,0])
    # print(s.plusOne_1([1,2,3]) == [1,2,4] )
    #
    # print(s.plusOne_2([0]))
    # print(s.plusOne_2([9]))
    # print(s.plusOne_2([1,2,3]))

# 
# if __name__ == '__main__':
#     main()
