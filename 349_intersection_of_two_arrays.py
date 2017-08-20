'''
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].

Note:
Each element in the result must be unique.
The result can be in any order.
'''


class Solution:
    def intersection_1(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list(set(nums1) & set(nums2))

    def intersection_2(self, nums1, nums2):
        output = []
        if len(nums1) > len(nums2):
            for num in nums2:
                if num in nums1 and num not in output:
                    output.append(num)
        else:
            for num in nums1:
                if num in nums2 and num not in output:
                    output.append(num)
        return output

    def intersection_3(self, nums1, nums2):
        output = set()
        if len(nums1) > len(nums2):
            for num in nums2:
                if num in nums1:
                    output.add(num)
        else:
            for num in nums1:
                if num in nums2:
                    output.add(num)
        return list(output)


# def main():
#
#
# if __name__ == '__main__':
#     main()
