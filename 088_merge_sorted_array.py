'''
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n)
to hold additional elements from nums2.
The number of elements initialized in nums1 and nums2 are m and n respectively
'''

'''
If new memory can be used, we can merge two sorted array like the merge algorithm in the Merge SOrt

def merge(nums1, nums2):
    output = []

    while len(nums1) != 0 and len(nums2) != 0:
        if nums1[0] >= nums2[0]:
            output.append(nums1[0])
            nums1.pop(0)
        else:
            output.append(nums2[0])
            nums2.pop(0)

        if len(nums1) == 0:
            output.extend(nums2)
        else:
            output.extend(nums1)
        return output
'''

class Solution:
    def merge_1(self,nums1, m, nums2, n):
        '''
        idea: brute force
        combine the nums2 into nums1 and use the sorting algorithm.
        however, the big O is O(nlogn).... not ideal
        because nums1 and nums2 are both sorted.

        For example:
        Example 1:
        nums1 = [0]
        m = 0
        nums2 = [1]
        n = 1

        Then, nums1 = [1]

        Example 2:
        nums1 = [1,3,5,0,0]
        m = 3
        nums2 = [2,6]
        n = 2

        then, nums1 = [1,2,3,5,6]

        '''
        if m == 0: # copy all elements in nums2 into nums1
            for i in range(len(nums2)):
                nums1[i] = nums2[i]
            return

        elif n == 0:
            return

        for i in range(n):
            nums1[m+i] = nums2[i]
        nums1.sort()

    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """

        '''
        idea:
        remember the elements after mth element in nums1 are not valid elements
        for example:
        nums1 = [1,2,5,7,0,0,0], m = 7
        nums2 = [3,4,8], n = 3

        compare the each element in nums1 (i = 0,.. m-1) and each element in nums2 (j = 0,...,n-1)
        replace the element in the last position with the bigger element of nums1 or nums1,
        then move the last position forward

        for example:
        nums1 = [1,2,5,7,0,0,0], m = 7
        nums2 = [3,4,8], n = 3

        i = 3, j = 2, last = m + n -1 = 4 + 3 - 1 = 6

        Until i == 0 or j == 0 (exit loops)
            Loop 1:
                step 1: compare nums1[3] = 7 and nums2[2] = 8
                step 2: replace nums1[6] = nums2[2]
                step 3: last = last - 1, j = j - 1

                Status:
                    nums1 = [1,2,5,7,0,0,8]
                    nums2 = [3,4,8]
                    i = 3, j = 1, last = 5

            Loop 2:(repeat step 1 to step 3)
                step 1: compare nums1[3] = 7 and nums2[1] = 4
                step 2: replace nums1[5] = nums1[3]
                step 3: last = last - 1, i = i - 1

                Status:
                    nums1 = [1,2,5,7,0,7,8]
                    nums2 = [3,4,8]
                    i = 2, j = 1, last = 4

            Loop 3:
                step 1: compare nums1[2] = 5 and nums2[1] = 4
                step 2: replace nums1[4] = nums1[2]
                step 3: last = last - 1, i = i - 1

                Status:
                    nums1 = [1,2,5,7,5,7,8]
                    nums2 = [3,4,8]
                    i = 1, j = 1, last = 3

            Loop 4:
                step 1: compare nums1[1] = 3 and nums2[1] = 4
                step 2: replace nums1[3] = nums2[1]
                step 3: last = last - 1, j = j - 1

                Status:
                    nums1 = [1,2,5,4,5,7,8]
                    nums2 = [3,4,8]
                    i = 1, j = 0, last = 2

            Loop 5:
                step 1: compare nums1[1] = 2 and nums2[0] = 3
                step 2: replace nums1[2] = nums2[0]
                step 3: last = last - 1, j = j - 1

                Status:
                    nums1 = [1,2,3,4,5,7,8]
                    nums2 = [3,4,8]
                    i = 1, j = 0, last = 2





        '''
        last = m + n - 1
        i = m - 1  #the index in nums1
        j = n - 1  #the index in nums1

        while i >= 0  and j >= 0:
            if nums1[i] >= nums2[j]:
                nums1[last] =nums1[i]
                i -= 1
            else:
                nums1[llast] = nums2[j]
                j -= 1
            last -= 1

        #  check the any element left in nums2:
        #  it may happen i == 0.
        #  it means the rest of element in nums2 are small then all elements in nums1
        while j >= 0:
            nums1[last] = nums2[j]
            last -= 1
            j -= 1






def main():
    s = Solution()
    nums1 = [0]
    nums2 = [1]
    m = 0
    n = 1
    s.merge_1(nums1, m, nums2, n)
    print(nums1)

if __name__ == '__main__':
    main()
