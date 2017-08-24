'''
Determine whether an integer is a palindrome. Do this without extra space.

click to show spoilers.

Some hints:
Could negative integers be palindromes? (ie, -1)

If you are thinking of converting the integer to string,
note the restriction of using extra space.

You could also try reversing an integer.
However, if you have solved the problem "Reverse Integer",
you know that the reversed integer might overflow. How would you handle such case?
There is a more generic way of solving this problem.
'''
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        '''
        idea:
        brute force, convert integer to string
        but use extra space.....bad!!
        '''
        if x >= 0:
            x = str(x)
            length = len(x)
            for i in range(length//2):
                if x[i] != x[length-i-1]:
                    return False
            return True
        else:
            return False



    def isPalindrome_2(self, x):
        if x >=0:
            return x == self.reverseInteger(x)
        else:
            return False

    def reverseInteger(self,x):
        #  do not convert integer to string
        #  only convert the non-negative integer
        output = 0

        while x > 0:
            digit = x % 10
            output += digit
            output *= 10
            x = x // 10
        return output // 10



def main():
    s = Solution()
    # print(s.isPalindrome_1(-1) == False)
    # print(s.isPalindrome_1(0) == True)
    # print(s.isPalindrome_1(123) == False)
    # print(s.isPalindrome_1(202) == True)

    print(s.isPalindrome_2(-1) == False)
    print(s.isPalindrome_2(0) == True)
    print(s.isPalindrome_2(123) == False)
    print(s.isPalindrome_2(202) == True)






if __name__ == '__main__':
    main()
