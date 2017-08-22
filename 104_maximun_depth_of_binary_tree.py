
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

'''
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes
along the longest path from the root node down to the farthest leaf node.
'''
class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        '''
        Tree1 depth = 3               Tree2 depth = 4
               A                           3
              / \                         / \
             B   C                       4   4
                / \                     /
               D   E                   2
                                      /
                                     3
        idea:
        use reursion to solve this probelm.
        if node exist, level = 1
        if node.left exists or node.right exists, go one level down,
        level += max (the max level right node has, the max level the left node has)

        For example,
        Tree1 depth = 3
               A
              / \
             B   C
                / \
               D   E

        D = 1 + level or none = 1 + 0 = 1
        E = 1 + level of none = 1 + 0 = 1 
        C = 1 + max(level of D or E) =  1 + 1 = 2
        B = 1 + level of node = 1
        A = 1 + max(level of B or C) = 1 + max(1,2) = 1 + 2 = 3
        '''

        return self.maxDepthHelper(root)

    def maxDepthHelper(self, node):
        if node is None:
            return 0

        level = 1
        if node.left or node.right:
            level += max(self.maxDepthHelper(node.left), self.maxDepthHelper(node.right))
        return level


# def main():
#     '''
#     create a binary tree
#     Tree1 depth = 3
#            A
#           / \
#          B   C
#             / \
#            D   E
#     '''
#     root = Node('A')
#     root.left = Node('B')
#     root.right = Node('C')
#     root.right.left = Node('D')
#     root.right.right = Node('E')
#
#     s = Solution()
#     print(s).maxDepth(root))
#
#
# if __name__ == '__main__':
#     main()
