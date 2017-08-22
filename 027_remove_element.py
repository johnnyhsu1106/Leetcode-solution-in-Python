'''
Given an array and a value, remove all instances of that value in place and return the new length.
Do not allocate extra space for another array, you must do this in place with constant memory.
The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example:
Given input array nums = [3,2,2,3], val = 3

Your function should return length = 2, with the first two elements of nums being 2.
'''
class Solution:
    def removeElement_1(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        '''
        edge case:
        if nums = [], return 0

        Idea1:
        For example, lst = [3,2,2,3], val = 3
        Use while loop, start with index = 0 , check each element equal to the val or not.
        if element is equal to val, pop the element, index stays still
        if element is not equal to val, increase the index

        '''

        if len(nums) == 0:
            return 0
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
            else:
                i += 1
        return len(nums)


# def main():
#     s = Solution()
#     print(s.removeElement_1([], 2) == 0)
#     print(s.removeElement_1([2],3) == 1)
#     print(s.removeElement_1([3,2,2,3], 3) ==2)
#
#
#
# if __name__ == '__main__':
#     main()
