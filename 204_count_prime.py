'''
Description:
Count the number of prime numbers less than a non-negative number, n.
'''
import math
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n < 3:
            return 0
        if n == 3:
            return 1

        count = 1
        for i in range(3,n,2):
            if self.isPrime_3(i):
                count += 1
        return count


    def isPrime_1(self, num):
        '''
        idea: the factor of prime number is 1 and prime number itself.
        However, the rumtime of this method is O(n)... not efficient
        '''
        if num == 2:
            return True

        n = 2
        while n < num:
            if num % n == 0:
                return False
            n += 1
        return True

    def isPrime_2(self, num):
        '''
        idea:
        approve the isPrime_1
        The rumtime of this alogrithm is O(n/2)
        '''
        if num == 2:
            return True
        if num % 2 == 0:
            return False

        n = 3
        #  start with 3, increase 2 (only validate odd number)
        while n < num:
            if num % n == 0:
                return False
            n += 2
        return True

    def isPrime_3(self, num):
        '''
        idea:
        if ay given n < sqrt(num), sqrt(num) % n != 0, then num is prime number
        The runtime of this algorithm is O(sqrt(n)/2)
        '''
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        n = 3
        # while n <= math.floor(math.sqrt(num)):
        # this syntax above is equal to the folowing one. but the following one is faster
        while n*n <= num:
            if num % n == 0:
                return False
            n += 2
        return True

#
# def main():
#     s = Solution()
    # print(s.isPrime(2) == True)
    # print(s.isPrime(3) == True)
    # print(s.isPrime(4) == False)
    # print(s.isPrime_2(5) == True)
    # print(s.isPrime(13) == True)

#     print(s.countPrimes(2))
#     print(s.countPrimes(4))
#     print(s.countPrimes(5))
#     print(s.countPrimes(999983))
#     print(s.countPrimes(1500000))
#
#
#
# if __name__ == '__main__':
#     main()
