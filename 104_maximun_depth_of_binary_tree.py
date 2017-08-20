
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
