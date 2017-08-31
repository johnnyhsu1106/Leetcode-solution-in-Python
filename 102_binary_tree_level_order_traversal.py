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
        '''
        idea:
        Use the while loop to traverse all nodes in each level.
        us
        '''

        if root is None:
            return []


        result = []
        current_level = [root] # a list stores all nodes in same level, initial value is [root]

        while current_level: # while len(current) > 0:
            next_level = []  # a list stores all nodes in next level
            values = []      # a list stores all nodes' value
            for node in current_level:
                values.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            current_level = next_level # update the current_level with next_level
            result.append(values)
        return result
