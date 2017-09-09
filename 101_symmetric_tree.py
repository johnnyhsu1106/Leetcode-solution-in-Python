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
    def __repr__(self):
        return str(self.val)

class Solution:
    def isSymmetric_1(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        '''
        tree
                1
              /  \
             2    2
            / \   / \
           3   4  4  3
          / \ /\  /\  / \
         5  6 7 8 8 7 6  5
        idea:
        If tree is symmetric,
        node.left.val == node.right.val
        node.left.left.val == node.right.rigt.val
        node.left.right.val == node.right.left.val

        node.left.left.left.val = node.right.right.right.val
        node.left.left.right.val = node.right.right.left.val
        node.left.right.left.val = node.right.left.right.val
        ... so on
        So use the recursive method call to solve this problem.

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
        1. Reverse the root.right
                1
               / \
              2   2
             / \ / \
            3  4 3  4
        2. Compare the sub-tree of root.left and sub-tree of root.right.
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

        node.left, node.right = node.right, node.left
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

    def isSymmetric_3(self, root):
        '''
        tree
                1
               / \
              2   2
             / \ / \
            3  4 4  3

        idea:
            use the stack to store
        '''
        if not root:
            return True

        stack = [root.left, root.right]
        while stack:
            p, q = stack.pop(), stack.pop()
            if not p and not q:
                continue
            elif not p or not q or p.val != q.val:
                return False
            stack.append(p.left)
            stack.append(q.right)
            stack.append(p.right)
            stack.append(q.left)
        return True



    def isSymmetric_4(self, root):
        '''
        tree
                1
               / \
              2   2
             / \ / \
            3  4 4  3
        idea:
        Use deque to solve this problem
        Traveser each level of binary tree and in the same time, pop the element in the front and rear.
        The two nodes' value should be the same if tree is symmetric
        '''
        if not root:
            return True

        curr_level = [root.left, root.right]

        while curr_level:
            next_level = []
            for node in curr_level:
                if node:
                    next_level.append(node.left)
                    next_level.append(node.right)
            while curr_level:
                p = curr_level.pop(0)
                q = curr_level.pop()

                if not p and not q:
                    continue
                elif not p or not q or p.val != q.val:
                    return False
            curr_level = next_level

        return True


# def main():
#     '''
#         1
#        / \
#       2   2
#      / \ / \
#     3  4 4  3
#     '''
#     root = TreeNode(1)
#     root.left = TreeNode(2)
#     root.right = TreeNode(2)
#     root.left.left = TreeNode(3)
#     root.left.right = TreeNode(4)
#     root.right.left = TreeNode(4)
#     root.right.right = TreeNode(3)
#
#     s = Solution()
#     print(s.isSymmetric_3(root))
#
# if __name__ == '__main__':
#     main()
