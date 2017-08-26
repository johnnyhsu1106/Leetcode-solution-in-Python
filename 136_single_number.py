'''
Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
'''

class Solution:
    def singleNumber_1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        idea:
        1. Use the dictionary (hashmap) to count the element. Cons : extra memory
        2. Bit manipulation: O(n), no extra memory
        3. sort nums and compare the each two elements. Cons: O(nlogn)
        '''
        nums_dict = { }
        for num in nums:
            if num not in nums_dict:
                nums_dict[num] = 0
            nums_dict[num] += 1

        for key in nums_dict:
            if nums_dict[key] == 1:
                return key

    def singleNumber_2(self, nums):
        return reduce(operator.xor, nums)

    def singleNumber_3(self, nums):

        if len(nums) == 1:
            return nums[0]
        nums.sort()
        for i in range(len(nums)//2):
            if nums[2*i] != nums[2*i+1]:
                return nums[2*i]
        return nums[-1]

# def main():
#     nums = [17,12,5,-6,12,4,17,-5,2,-3,2,4,5,16,-3,-4,15,15,-4,-5,-6]
#     s = Solution()
#     print(s.singleNumber_3(nums))
#
# if __name__ == '__main__':
#     main()
