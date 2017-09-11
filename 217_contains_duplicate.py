'''
Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice in the array,
and it should return false if every element is distinct.
'''
from collections import defaultdict

class Solution:
    def containsDuplicate_1(self, nums):
        return len(nums) > len(set(nums))


    def containsDuplicate_2(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) <= 1:
            return False

        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False


    def containsDuplicate_3(self, nums):
        nums_dict = defaultdict(int)
        for num in nums:
            nums_dict[num] += 1
            if nums_dict[num] > 1:
                return True
        return False
