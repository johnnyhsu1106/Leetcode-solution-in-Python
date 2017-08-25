'''
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        '''
        idea: insert the node for middle element of array,
        Then, insert middle of left arry recursively

        insert middle of right array recursively
        until all elemnt is inserted into the binary tree

        for example:
        [1,2,3,4,5,6,7]
              4
            /   \
           2     6
          / \   / \
         1   3  5  7
        '''
