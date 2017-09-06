'''
Given an array of size n, find the majority element.
The majority element is the element that appears more than ⌊ n/2 ⌋ times.
You may assume that the array is non-empty and the majority element always exist in the array.
'''

class Solution:
    def majorityElement_1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return nums[0]

        num_dict = {}
        for num in nums:
            if num not in num_dict:
                num_dict[num] = 0
            num_dict[num] += 1
            if num_dict[num] > n//2:
                return num


    def majorityElement_2(self, nums):
        index, count = 0, 1

        for i in range(1, len(nums)):
            if nums[index] == nums[i]:
                count += 1
            else:
                count -= 1
                if count == 0:
                    index = i
                    count = 1

        return nums[index]
