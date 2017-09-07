'''
Given a non-empty binary search tree and a target value,
find the value in the BST that is closest to the target.
Note:
Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to the target.
'''

# Time:  O(h)
# Space: O(1)
def buildBSTFromSortedArray(lst):
    if len(lst) == 0:
        return

    return buildTree(lst, 0, len(lst)-1)

def buildTree(lst, start, end):
    if start > end:
        return

    root = TreeNode(lst[start + (end-start)//2])
    root.left = buildTree(lst, start, start + (end-start)//2 -1)
    root.right = buildTree(lst, start + (end-start)// 2 +1 , end)

    return root



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        '''
        idea:
        Unlike bst search method, search the target by calling search method recursively.

        def search(root, target):
            if target == root.val:
                return root.val
            elif target < root.val:
                search(root.left, target)
            else:
                search(root.right, target)

        I choose to use while loop so we can search from root to leave and then we calculate the gap
        between each node and target, at meantimes track the closest node
        '''
        node = root
        gap = float('inf')
        closest = root

        while node:

            if abs(target - node.val) < gap:
                gap = abs(target - node.val)
                closest = node

            # decide the next node for calculating the gap
            if target == node.val:
                break
            elif target < node.val:
                node = node.left
            else:
                node = node.right

        return closest.val


#
# def main():
#     s = Solution()
#     '''
#            6
#          /   \
#         4     8
#       /  \   /  \
#      3   5  7    9
#     '''
#     root = buildBSTFromSortedArray([x for x in range(3,10)])
#     print(s.closestValue(root, 6.1))
# 
#
# if __name__ == '__main__':
#     main()
