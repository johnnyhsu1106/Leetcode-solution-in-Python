'''
Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space.
You may not modify the values in the list, only nodes itself can be changed.

'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs_1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        '''
        The first solution is to swap the value of the node.
        The second solution is to swap the node without changing its value.
        '''
        if not head or not head.next:
            return head
        prev_node = None
        curr_node = head
        idx = 1
        while curr_node:
            if idx % 2 == 0:
                prev_node.val, curr_node.val = curr_node.val, prev_node.val

            prev_node = curr_node
            curr_node = curr_node.next
        return head


    def swapPairs_2(self, head):
        '''
        idea:
        create a dummy node as the head of linked list
        return the dummy.next
        '''
        dummy = ListNode(0)
        dummy.next = head
        curr_node = dummy

        while curr_node.next and curr_node.next.next:
            next_one = curr_node.next
            next_two = curr_node.next.next
            next_three = curr_node.next.next.next

            curr_node.next = next_two
            next_two.next = next_one
            next_one.next = next_three
            curr_node = next_one
        return dummy.next
