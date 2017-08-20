'''
Given two binary trees, write a function to check if they are equal or not.
Two binary trees are considered equal if they are structurally identical and the nodes have the same value.
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        #  Base case: check the p , q exist
        #  if p and q, both node don't exist, return True
        if not p and not q:
            return True
        # if p or q, either doen't exist, return False
        elif not p and q or p and not q:
            return False

        # at same level, check the value of p and q are equal
        if p and q:
            if p.val != q.val:
                return False

        #  check next level (left node and right node) recursively
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
