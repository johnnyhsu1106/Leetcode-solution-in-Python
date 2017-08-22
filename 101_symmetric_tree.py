'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3

But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric_1(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        '''
        if tree is symmetric,
        the node.left.val == node.right.val
        the node.left.left.val == node.right.rigt.val
        the node.left.right.val == node.right.left.val

        ... so on

        '''
        if not root:
            return True
        return self.isSymmetric_1_helper(root.left, root.right)

    def isSymmetric_1_helper(self, left, right):

        if not left and not right:
            return True

        if not left or not right or left.val != right.val:
            return False

        return self.isSymmetric_1_helper(left.left, right.right) and self.isSymmetric_1_helper(left.right, right.left)



    def isSymmetric_2(self, root):
        '''
        tree
                1
               / \
              2   2
             / \ / \
            3  4 4  3

        idea:
        1. reverse the root.right
                1
               / \
              2   2
             / \ / \
            3  4 3  4
        2. compare the sub-tree of root.left and sub-tree of root.right.
            if two sub-trees are the same, then the tree is symmetric tree
              2      2
             / \    / \
            3  4   3   4
        '''
        if not root:
            return True
        elif (not root.left and root.right) and (root.left and not root.right):
            return False
        elif not root.left and not root.right:
            return True

        self.invertTree(root.right)
        return self.isSameTree(root.left, root.right)



    def invertTree(self, node):
        '''
        Please check the leetcode problem 228
        '''
        if not node:
            return

        temp = node.left
        node.left = node.right
        node.right = temp

        self.invertTree(node.left)
        self.invertTree(node.right)



    def isSameTree(self, node1, node2):
        '''
        Please check the leetcode problem 100
        '''
        if not node1 and not node2:
            return True

        elif (not node1 and node2) or (node1 and not node2):
            return False

        elif node1.val != node2.val:
            return False

        return self.isSameTree(node1.left, node2.left) and self.isSameTree(node1e.right, node2.right)
