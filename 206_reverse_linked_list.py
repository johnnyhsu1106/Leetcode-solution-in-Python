'''
Reverse a singly linked list.
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current_node = head
        previous_node = None
        while current_node:

            next_node = current_node.next
            # chanage the pointer
            current_node.next = previous_node
            # move on to next node
            previous_node = current_node
            current_node = next_node

        head = previous_node
        return head
