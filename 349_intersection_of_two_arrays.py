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
        '''
        idea:
        Time: O(n^2)... bad
        '''
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
        '''
        idea:
        Time: O(n^2)... bad
        '''
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

    def intersection_4(self, nums1, nums2):
        '''
        idea:
        Time: best case: O(max(m,n))...good
              worst case: O(m+n)
        '''
        nums1.sort()
        nums2.sort()
        i, j = 0, 0

        result = set()
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                result.add(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return list(result)


    def intersection_5(self, nums1, nums2):
        '''
        '''
        result = []

        if len(nums1) > len(nums2):
            long_nums = nums1
            short_nums = nums2
        else:
            long_nums = nums2
            short_nums = nums1

        # lookup = set(long_nums)... this is equal to the line 90 - 92
        lookup = set()
        for num in long_nums:
            lookup.add(num)

        for num in short_nums:
            if num in lookup:
                result.append(num)
                lookup.discard(num)
        return result


# 
# def main():
#     nums1 =[1,3,2]
#     nums2 = [2,7,6]
#     s = Solution()
#     print(s.intersection_5(nums1, nums2))
#
# if __name__ == '__main__':
#     main()
