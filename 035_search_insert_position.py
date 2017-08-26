'''
Given a sorted array and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0
'''

class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        '''
        idea:
        use binary search to solve this problem becasue the nums is "sorted".
        1. binary search - recursive implementation
        2. binary search - iterative implementation (choose this one)
        '''
        left = 0
        right = len(nums)-1

        while left <= right:
            mid = left + (right  - left) // 2 # avoid overflow

            if target == nums[mid]:
                break
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        if nums[mid] == target:
            return mid
        return left

# def main():
#     '''
#     Here are few examples.
#     [1,3,5,6], 5 → 2
#     [1,3,5,6], 2 → 1
#     [1,3,5,6], 7 → 4
#     [1,3,5,6], 0 → 0
#     '''
#     s = Solution()
#     print(s.searchInsert([1,3,5,6],5) == 2)
#     print(s.searchInsert([1,3,5,6],2) == 1)
#     print(s.searchInsert([1,3,5,6],7) == 4)
#     print(s.searchInsert([1,3,5,6],0) == 0)
#
# if __name__ == '__main__':
#     main()
