'''
Given a sorted array, remove the duplicates in place
such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
It doesn't matter what you leave beyond the new length.
'''

class Solution:
    def removeDuplicates_1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        elif len(nums) ==1:
            return 1

        i = 0
        while i < len(nums) - 1:
            if nums[i+1] == nums[i]:
                nums.pop(i+1)
            else:
                i += 1
        return nums



    def removeDuplicates_2(self, nums):
        if len(nums) == 0:
            return 0
        elif len(nums) ==1:
            return 1

        i = 1
        last = 0
        while i < len(nums):
            if nums[last] != nums[i]:
                last += 1
                nums[last] = nums[i]


            i += 1
        return last + 1


# def main():
#     s = Solution()
#     print(s.removeDuplicates_1([]))
#     print(s.removeDuplicates_1([1]))
#     print(s.removeDuplicates_1([1,1,2,3,3,3]))
#
#
#     print(s.removeDuplicates_2([]))
#     print(s.removeDuplicates_2([1]))
#     print(s.removeDuplicates_2([1,1,2,3,3,3]))
#
#
#
# if __name__ == '__main__':
    # main()
