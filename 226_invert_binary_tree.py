class TreeNode:
    def __init__(self, value):
        self.val = value
        self.right = None
        self.left = None

'''
Invert a binary tree.

     4
   /   \
  2     7
 / \   / \
1   3 6   9
to
     4
   /   \
  7     2
 / \   / \
9   6 3   1
'''

class Solution:
    def invertTree_1(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        '''
        Time: O(n), n is the total number of nodes
        '''
        if root is None:
            return

        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

    def invertTree_2(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root:
            temp = root.left
            root.left = root.right
            root.right = temp
            self.invertTree_2(root.left)
            self.invertTree_2(root.right)
            return root


    def invertTree_3(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        '''
        idea:
                 4
               /   \
              2     7
             / \   / \
            1   3 6   9
        traverse all nodes in the binary tree by using stack/queue
        1. initialize the stack, stack = [root]
        2. pop the node from stack and swap the node's left and node's right
        3. if node's left exists, push node's left into stack
            if node's left exists, push node's left into stack
        4. repeat 2 and 3, until stack is empty

        note: use stack/queue. are good. However, list.pop() is more efficient than list.pop(0)
        '''
        if root == None:
            return root

        stack = [root]
        while len(stack) != 0:
            node = stack.pop() #node =stack.pop(0)
            node.left, node.right = node.right, node.left
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return root
