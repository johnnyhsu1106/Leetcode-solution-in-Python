'''
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

Note:
Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.

Follow up:
What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that
you cannot load all elements into the memory at once?
'''
import collections
class Solution:
    def intersect_1(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        output = []
        if len(nums1) == 0 or len(nums2) == 0:
            return output

        if len(nums1) > len(nums2):
            for i in range(len(nums2)):
                num = nums2[i]
                if num in nums1:
                    output.append(num)

                    nums1[nums1.index(num)]= None
                    nums2[i] = None
        else:
            for i in range(len(nums1)):
                num = nums1[i]
                if num in nums2:
                    output.append(num)
                    nums2[nums2.index(num)] = None
                    nums1[i] = None
        return output


    def intersect_2(self, nums1, nums2):
        c = collections.Counter(nums1) & collections.Counter(nums2)
        intersect = []
        for i in c:
            intersect.extend([i] * c[i])
        return intersect
