'''
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined
as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        '''
        idea:
        For each node, the difference of left node's depth and rihgt node's depth can be greater than 1.
        First, write a method to calculate the depth of each node (please see leetcode problem 104)
        Second, write a helper method to go through each left node and right node
        Then, call its self method recursively. (visit the left node and right node below) 

        '''

        return self.isBalanced_helper(root)

    def isBalanced_helper(self, node):
        if not node:
            return True

        elif not node.left and not node.right:
            return True

        elif node.left or node.right:
            if math.fabs(self.depth(node.left) - self.depth(node.right)) > 1:
                return False

        return self.isBalanced_helper(node.left) and self.isBalanced_helper(node.right)



    def depth(self, node):
        if not node:
            return 0

        level = 1
        if node.left or node.right:
            level += max(self.depth(node.left), self.depth(node.right))
        return level
