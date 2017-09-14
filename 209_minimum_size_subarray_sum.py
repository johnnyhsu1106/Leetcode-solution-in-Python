'''
Given an array of n positive integers and a positive integer s,
find the minimal length of a contiguous subarray of which the sum ≥ s.
If there isn't one, return 0 instead.

For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.

click to show more practice.

More practice:
If you have figured out the O(n) solution,
try coding another solution of which the time complexity is O(n log n).
'''
class Solution(object):
    def minSubArrayLen_1(self, s, nums):
        '''
        idea:
        The most common way is to use two for loop. However, time complexity is too hight.
        Time: O(n^2)
        '''
        size = len(nums)
        if size == 0:
            return 0

        min_length = float('inf')
        for i in range(size):
            total = 0
            for j in range(i, size):
                total += nums[j]
                if total >= s:
                    min_length = min(min_length, j - i + 1)
                    break

        if min_length == float('inf'):
            return 0
        return min_length


    def minSubArrayLen_2(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        '''
        idea:
        Two pointers - Sliding window solution.
        '''
        size = len(nums)
        min_length = float('inf')
        j = 0
        total = 0
        for i in range(size):
            while j < size and total < s:
                total += nums[j]
                j += 1
            if total >= s:
                min_length = min(min_length, j - i )
                total -= nums[i]

        if min_length == float('inf'):
            return 0
        return min_length

# def main():
#     s = Solution()
#     # print(s.minSubArrayLen_1(7, [2,3,1,2,4,3]))
#     print(s.minSubArrayLen_2(7, [2,3,1,2,4,3]))
#
# if __name__ == '__main__':
#     main()
