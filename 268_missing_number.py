'''
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n,
find the one that is missing from the array.

For example,
Given nums = [0, 1, 3] return 2.

Note:
Your algorithm should run in linear runtime complexity.
Could you implement it using only constant extra space complexity?

'''
import collections
class Solution:
    def missingNumber_1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        idea:
        summation of 0,1,... n
        drawback: it may overflows..... if n is huge
        '''
        n = len(nums)
        return n*(n+1)//2 - sum(nums)


    def missingNumber_2(self, nums):
        '''
        idea:
        use map/dictionary to track each num.
        drawback: extra space.
        '''
        num_map = collections.defaultdict(int)
        for num in nums:
            num_map[num] = 1

        for i in range(len(nums)+1):
            if num_map[i] != 1:
                return i



# def main():
#     lst = [ i for i in range(0, 10)]
#     lst.pop(8)
#     print(lst)
#
#     s = Solution()
#     print(s.missingNumber_1(lst))
#     print(s.missingNumber_2(lst))
#
#
# if __name__ == '__main__':
#     main()
