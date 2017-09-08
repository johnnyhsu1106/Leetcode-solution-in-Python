'''
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
Note:
You may assume that the array does not change.
There are many calls to sumRange function.
'''
class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        '''
        idea:
        creat a array(list), whose size as the same of input.
        '''
        self.sum_nums = []
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            self.sum_nums.append(total)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0:
            return self.sum_nums[j]
        return self.sum_nums[j] - self.sum_nums[i-1]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

# def main():
#     nums_array = NumArray([-2, 0, 3, -5, 2, -1])
#     print(nums_array.sumRange(0,2))
#     print(nums_array.sumRange(2,5))
#     print(nums_array.sumRange(0,5))
#
# if __name__ == '__main__':
#     main()
