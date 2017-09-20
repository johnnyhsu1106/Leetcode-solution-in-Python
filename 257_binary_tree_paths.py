'''
Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

["1->2->5", "1->3"]
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def binaryTreePaths_1(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        output = []
        if root is None:
            return []
        self.findPath(root, '', output)
        return output

    def findPath(self, node, path, lst):
        '''
        idea: for any binary tree problem, the best solution is to imlement it recursively.
        concanate the path recursively
        '''
        #
        if node.left is None and node.right is None:
            lst.append(path + str(node.val))
        else:
            if node.left:
                self.findPath(node.left, path + str(node.val) + '->' , lst)
            if node.right:
                self.findPath(node.right, path + str(node.val)+ '->', lst)



    def binaryTreePaths_2(self, root):
        paths = []
        if not root:
            return paths

        left_paths = self.binaryTreePaths_2(root.left)
        right_paths = self.binaryTreePaths_2(root.right)


        for path in left_paths:
            paths.append(str(root.val) + '->' + path)

        for path in right_paths:
            paths.append(str(root.val) + '->' + path)

        if len(paths) == 0:
            paths.append(str(root.val))

        return paths



# def main():
#     '''
#        1
#      /   \
#     2     3
#      \
#       5
#     All root-to-leaf paths are:
#
#     ["1->2->5", "1->3"]
#     '''
#
#     root = TreeNode(1)
#     root.left = TreeNode(2)
#     root.right = TreeNode(3)
#     root.left.right = TreeNode(5)
#
#
#     s = Solution()
#     print(s.binaryTreePaths_1(root))
#     print(s.binaryTreePaths_2(root))
#
#
# if __name__ == '__main__':
#     main()
