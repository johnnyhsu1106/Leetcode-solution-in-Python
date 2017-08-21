'''
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
            
        fast = head.next
        slow = head

        while fast and fast.next:
            if fast is slow:
                return True

            fast = fast.next.next
            slow = slow.next
        return False
