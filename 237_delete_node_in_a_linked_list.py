# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

'''
Write a function to delete a node (except the tail) in a singly linked list,
given only access to that node.

Supposed the linked list is 1 -> 2 -> 3 -> 4 and you are given the third node with value 3,
the linked list should become 1 -> 2 -> 4 after calling your function.
'''
class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """

        node.val = node.next.val
        if node.next.next:
            node.next = node.next.next
        else:
            node.next = None

        '''
        The original idea is that
        if we can find the prev_node, then
        prev_node.next = node.next
        however; we can not find the prev_node
        so another idea is

        1. copy the node.next.val to node.val
        1 -> 2 -> 3 -> 4 -> 5
        become 1 -> 2 -> 4 -> 4 -> 5
        2. remove 4th node
        node.next = node.next.next


        '''

# def main():
#
#
# if __name__ == '__main__':
#     main()
