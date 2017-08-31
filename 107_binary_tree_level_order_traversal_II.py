'''
Given a binary tree, return the bottom-up level order traversal of its nodes' values.
(ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7]

   3
   / \
  9  20
    /  \
   15   7

return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom_1(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        '''
        idea:
        Check the problem 102, use while loop and for loop to traverse node in each level
        Then, get the result
        [
          [3],
          [9,20],
          [15,7]
        ]
        Then, reverse the result
        '''
        if root is None:
            return []

        result = []
        current_level = [root]
        while current_level:
            next_level = []
            values = []
            for node in current_level:
                values.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            current_level = next_level
            result.append(values)

        result.reverse() #  reverse the result

        return result


    # def levelOrderBottom_2(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: List[List[int]]
    #     """
    #     '''
    #     idea:
    #     recursive method
    #     '''
    #
    #     if root is None:
    #         return []
    #     lst = []
    #     self.levelOrderBottom_1_helper([root], lst)
    #     lst.reverse()
    #     return lst
    #
    # def levelOrderBottom_2_helper(self, current_level, lst):
    #     for node in current_level:
    #         lst.append(node.val)
    #     if self.left:
    #         current_level = [node.left]
    #     if
    #     self.levelOrderBottom_2_helper([node.left, lst)
    #     self.levelOrderBottom_2_helper(node.right, lst)
