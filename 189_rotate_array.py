'''
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.

Hint:
Could you do it in-place with O(1) extra space?
Related problem: Reverse Words in a String II
'''
class Solution:
    def rotate_1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        '''
        idea:
        Pop the last one element and insert into the first position for k times.
        pros: no need the extra space
        cons: the runtime of this algorithm is O(nk),
        '''
        for i in range(k): #O(k)
            num = nums.pop() # O(1)
            nums.insert(0,num) #O(n-1)

    def rotate_2(self, nums, k):
        '''
        idea:
        Use a list to store k elements and shift the element in nums
        pros: the runtime of this algorithm is O(n+k)
        cons: extra space O(1)
        '''


        lst = []
        for i in range(k):
            lst.append(nums[len(nums)-i-1])
        # lst = [7,6,5]

        for i in range(len(nums)-k):
            nums[len(nums)-i-1] = nums[len(nums)-k-1-i]
        # nums = [1,2,3,1,2,3,4]

        for i in range(k):
            nums[i] = lst[k-i-1]
        # nums= [5,6,7,1,2,3,4]

    # def rotate_3(self, nums, k):




# def main():
#     s = Solution()
#     #
#     # nums = [1,2,3,4,5,6,7]
#     # s.rotate_1(nums, 3)
#     # print(nums)
#
#     nums = [1,2,3,4,5,6,7]
#     s.rotate_2(nums, 4)
#     print(nums)
#
# if __name__ == '__main__':
#     main()
