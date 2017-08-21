'''
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia:
“The lowest common ancestor is defined between two nodes v and w as the lowest node in T
that has both v and w as descendants (where we allow a node to be a descendant of itself).”

        _______6______
       /              \
    ___2__          ___8__
   /      \        /      \
   0      _4       7       9
         /  \
         3   5
For example, the lowest common ancestor (LCA) of nodes 2 and 8 is 6.
Another example is LCA of nodes 2 and 4 is 2,
since a node can be a descendant of itself according to the LCA definition
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.val)

    def append(self, value):
        node = TreeNode(value)

        if value < self.val:
            if self.left:
                self.left.append(value)
            else:
                self.left = node
        else:
            if self.right:
                self.right.append(value)
            else:
                self.right = node

    def print_in_order(self):
        if self.left:
            self.left.print_in_order()

        print(self.val)

        if self.right:
            self.right.print_in_order()



class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        '''
        The common ancestor must  between the p and q based on the characteristic of binary search tree
        For example:
                _______6______
               /              \
            ___2__          ___8__
           /      \        /      \
           0      _4       7       9
                 /  \
                 3   5
        Find the lower common ancestor(LCA) of 2 and 8.
        6 is between 2 and 8 so 6 is the LCA 2 and 8

        If we want to find the LCA of 7 and 9
        How? .....
        Remember the LCA must be located btw p and q.
        because root (6) is small than 7 and 9
        replace root with root.right (go to find the node, which is greater than root)

        If find the LCA of 3 and 5
        root (6) is greater than 3 and 5
        so replace root with root.left
        root (2) is smaller than 3 and 5
        so replace the root with root.right
        root (4) is betwen 3 and 5....so we find it

        '''
        if p.val > q.val:
            small_node, large_node = q, p
        else:
            small_node, large_node = p, q

        while not (root.val >= small_node.val and root.val <= large_node.val):
            if root.val < small_node.val:
                root = root.right
            else:
                root = root.left
        return root
# ================= Test Area ==================
def main():
    root = TreeNode(6)
    append_lst = [2,8,0,4,7,9,3,5]
    for num in append_lst:
        root.append(num)

    s = Solution()
    p = TreeNode(4)
    q = TreeNode(7)
    print(s.lowestCommonAncestor(root,p,q))



if __name__ == '__main__':
    main()
