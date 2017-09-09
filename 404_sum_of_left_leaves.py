'''
Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def sumOfLeftLeavesHelper(root):
            '''
            notice:
            If this helper function only is used by outside function,
            it can be written inside the function.
            However, the inside function should be declared before calling it.
            Because of this declaration, the inside function will be called by outside function only.

            '''

            if not root:
                return 0

            result = 0
            if root.left:
                node = root.left
                if not node.left and not node.right:  # this node is leave
                    result += node.val
                else:                                 # find the next node (root.left)
                    result += sumOfLeftLeavesHelper(node)

            if root.right:
                node = root.right
                result += sumOfLeftLeavesHelper(node)

            return result

        return sumOfLeftLeavesHelper(root)

#
# def main():
#     '''
#         3
#        / \
#       9  20
#         /  \
#        15   7
#
#     '''
#     root = TreeNode(3)
#     root.left = TreeNode(9)
#     root.right = TreeNode(20)
#     root.right.left = TreeNode(15)
#     root.right.right = TreeNode(7)
#
#     s = Solution()
#     print(s.sumOfLeftLeaves(root) == 24)
#
#
# if __name__ == '__main__':
#     main()
