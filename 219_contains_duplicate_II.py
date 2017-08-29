'''
Given an array of integers and an integer k,
find out whether there are two distinct indices i and j in the array
such that nums[i] = nums[j] and the absolute difference between i and j is at most k.
'''
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums) <= 1:
            return False

        num_map = {} # key: value = num: [index1, index2,...]
        for i in range(len(nums)):
            num = nums[i]
            if num in num_map and i - num_map[num] <= k:
                return True
            else:
                num_map[num] = i
        return False




# def main():
#     s = Solution()
#     print(s.containsNearbyDuplicate([1,2,3,1], 2))
#     print(s.containsNearbyDuplicate([1,2,3,1], 4))
#     print(s.containsNearbyDuplicate([1,2,3,4], 4))
#
#
#
#
#
# if __name__ == '__main__':
#     main()
