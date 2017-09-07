'''
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.val)

    def print_each_level(self):
        current_level = [self]

        while len(current_level) != 0:
            next_level = []

            output = ''
            for node in current_level:
                output += str(node.val) + ' '
            print(output)

            for node in current_level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            current_level = next_level


class Solution:
    def sortedArrayToBST_1(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        '''
        idea:

        for example:
        [1,2,3,4,5,6,7]
              4
            /   \
           2     6
          / \   / \
         1   3  5  7
         Fetch the median of sorted array, [1,2,3,4,5,6,7], as root, such as 4.
         The median of left side array,[1, 2, 3], as root.left(root of sub-tree) such as 2.
         The median of right side array,[5, 6, 7], as root.right(root of sub-tree) such as 6.

         Recursively, do this process.

         You can use the two index(pointer) to record the position of first element and last position of sbu-array.
         Or use the slicing (python build in method) to get the median of sub-array
         1. Use two index: O(n)
         2. Use slicing: slower than first on

         This is the way to build a balanced binary search tree.
        '''
        if len(nums) == 0:
            return None

        return self.buildTree(nums, 0, len(nums)-1)


    def buildTree_1(self, nums, start, end):
        #  base case
        if start > end:
            return
        node = TreeNode(nums[(start + end) // 2])
        node.left = self.buildTree(nums, start, (start+end)//2 -1)
        node.right = self.buildTree(nums, (start+end)//2+1, end)
        return node





    def sortedArrayToBST_2(self, nums):
        if len(nums) == 0:
            return
        return self.buildTree_2(nums)

    def buildTree_2(self, nums):
        if len(nums) == 0:
            return

        length = len(nums)
        node = TreeNode(nums[length//2])
        node.left = self.buildTree_2(nums[:length//2])
        node.right = self.buildTree_2(nums[length//2+1:])
        return node




# def main():
    #  test the method: print_each_level

    # root = TreeNode(4)
    # root.left = TreeNode(2)
    # root.right = TreeNode(6)
    # root.left.left = TreeNode(1)
    # root.left.right = TreeNode(3)
    # root.right.left = TreeNode(5)
    # root.right.right = TreeNode(7)
    # root.print_each_level()

    # test the method sortedArrayToBST
    # s = Solution()
    # root = s.sortedArrayToBST_1([i for i in range(1,8)])
    # root.print_each_level()

    # root = s.sortedArrayToBST_2([i for i in range(1,8)])
    # root.print_each_level()


# 
# if __name__ == '__main__':
#     main()
