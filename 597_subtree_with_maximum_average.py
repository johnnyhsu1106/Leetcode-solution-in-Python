'''
Given a binary tree, find the subtree with maximum average. Return the root of the subtree.

Example
Given a binary tree:

     1
   /   \
 -5     11
 / \   /  \
1   2 4    -2
return the node 11.
'''
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""


class Solution:
    """
    @param: root: the root of binary tree
    @return: the root of the maximum average of subtree
    """

    max_avg = float('-inf')
    subtree = None

    def findSubtree2(self, root):
        self.subtree_avg(root)
        return self.subtree

    def subtree_avg(self, node):
        if not node:
            return 0, 0

        left_sum, left_size = self.subtree_avg(node.left)
        right_sum, right_size = self.subtree_avg(node.right)
        total_sum = left_sum + right_sum + node.val
        total_size = left_size + right_size + 1
        avg = float(total_sum) / total_size #covert the int to float. so the float division will be correct.

        if avg >= self.max_avg:
            self.max_avg = avg
            self.subtree = node

        return total_sum, total_size
