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

        Idea:
        Use while loop, start with index = 0 , check each element equal to the val or not.
        If element is equal to val, pop the element, index stays still
        If element is not equal to val, increase the index

        For example, nums = [3,2,2,3], val = 3
        i = 0 < len(nums)=4: nums[0] = 3, nums.pop(0) -> nums = [2,2,3]
        i = 0 < len(nums)=3: nums[0] = 3, i += 1, then i = 1
        i = 1 < len(nums)=3: nums[1] = 2, i += 1, then i = 2
        i = 2 < len(nums)=3: nums[2] = 3, nums.pop(2) -> nums= [2,2,3]
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



    def removeElement_2(self, nums, val):
        '''
        edge case:
        if nums = [], return 0

        idea:
        i = 0 , last = len(nums)-1
        If element is equal to val,
        swap the element, which is equal to value, with the element with index = last in the array
        Then move the index last forward (last -= 1)

        If element is not equal to val,
        increase the i

        Keep doing this, until i > last

        Finally, return last + 1

        For example, nums = [3,2,2,3], val = 3
        i = 0, last = len(nums) -1 = 3
        nums = [3,2,2,3], last = 3 -1 = 2

        i = 0, last = 2
        nums =[2,2,3,3], i = 0 + 1 = 1

        i = 1, last = 2
        nums = [2,2,3,3], i = 1 + 1 = 2

        i = 2, last = 2
        nums = [2,2,3,3], last = 2 - 1 = 1

        return last + 1

        '''

        if len(nums) == 0:
            return 0

        i = 0
        last = len(nums) -1

        while i <= last:
            if nums[i] == val:
                nums[i], nums[last] = nums[last], nums[i]
                last -= 1
            else:
                i += 1

        return last + 1



# def main():
#     s = Solution()
#     print(s.removeElement_1([], 2) == 0)
#     print(s.removeElement_1([2],3) == 1)
#     print(s.removeElement_1([3,2,2,3], 3) ==2)
#
#     print(s.removeElement_2([], 2) == 0)
#     print(s.removeElement_2([2],3) == 1)
#     print(s.removeElement_2([3,2,2,3], 3) ==2)
#
#
# if __name__ == '__main__':
#     main()
