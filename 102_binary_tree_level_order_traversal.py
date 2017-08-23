'''
Given a binary tree, return the level order traversal of its nodes' values.
(ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        lst = []
        return self.levelOrder_helper(node, lst)


    def levelOrder_helper(self, node, lst):
        if not node:
            return lst

        return lst.append([node.val])

        if node.left:
            lst.extend(self.levelOrder_helper(node.left, lst))
        if node.right:
            lst.extend(self.levelOrder_helper(node.right, lst))
