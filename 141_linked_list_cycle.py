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

        '''
        idea:
        use two marker, called fast and slow, traverse the linked list.
        fast is always moving foward linked list faster than slow.
        fast move two steps at a time and slow moves one steps at a time.
        During the traversal of linked list, if fast meets slow, it measn the linked lis has a cycle
        or it won't meet each other forever becasue it is a one way linked list.
        '''
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
