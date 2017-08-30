'''
Given a binary tree and a k, determine
if the tree has a root-to-leaf path
such that adding up all the values along the path equals the given k.

For example:
Given the below binary tree and k = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which k is 22.
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root, k):
        """
        :type root: TreeNode
        :type n: int
        :rtype: bool
        """
        '''
        idea:

        The whole idea is to use subtraction.
        From root to leave, we try to find the leave node, a node without any child.
        (node.left and node.right are both equal to None)
        and node's val is equal to the k substract all the sum of all nodes' val from root

        use the following binary tree as a example.
        Given the below binary tree and k = 22,
                      5
                     / \
                    4   8
                   /   / \
                  11  13  4
                 /  \      \
                7    2      1
        First, start with the root, check if node is None, return False
        Second, check if node.left is None and node.right is None and node.val == k, return True
        Third, call itself recursively, pass node.left/node.right and the k - node.val as new argument

        '''
        # base case 1
        if root is None:
            return False

        # bae case 2
        # if root is leave
        if root.left is None and root.right is None and root.val == k:
            return True

        return self.hasPathSum(root.left,  k - root.val) or self.hasPathSum(root.right,  k - root.val)
