'''
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path
from the root node down to the nearest leaf node.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.depth(root)

    def depth(self, node):
        if node is None:
            return 0

        if node.left and node.right:
            return min(self.depth(node.left), self.depth(node.right)) + 1
        else:
            return max(self.depth(node.left), self.depth(node.right)) + 1
