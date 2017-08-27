'''
Given an array of integers,
return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

class Solution:
    def twoSum_1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        '''
        idea:
        brute force ... use two loop
        '''

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]

    def twoSum_2(self, nums, target):
        '''
        idea:
        use extra memory to track the num and index, such as dictionary(hashmap)

        '''

        nums_dict = {}
        for i in range(len(nums)):
            num = nums[i]
            if num in nums_dict:
                return [nums_dict[num], i]
            else:
                nums_dict[target - num] = i
