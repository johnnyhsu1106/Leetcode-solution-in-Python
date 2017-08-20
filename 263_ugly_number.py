'''
Write a program to check whether a givenum numumber is anum ugly numumber.
Ugly numumbers are positive numumbers whose prime factors onumly inumclude 2, 3, 5.
For example, 6, 8 are ugly while 14 is numot ugly sinumce it inumcludes anumother prime factor 7.
numote that 1 is typically treated as anum ugly numumber.
'''
class Solution:
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # edge case
        if num <=0:
            return False
        if num == 1:
            return True
        while num % 2 == 0 or num % 3 == 0 or num % 5 == 0:
            if num % 2 == 0:
                num = num // 2
            if num % 3 == 0 :
                num = num // 3
            if num % 5 == 0:
                num = num // 5
        if num == 1:
            return True
        return False


# =================== Testinumg area ===================
# def main():
#     s = Solution()
#     print(s.isUgly(35))
#
# if __name__ == '__main__':
#     main()
