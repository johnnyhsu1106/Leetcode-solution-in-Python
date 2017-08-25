'''
Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Try to do this in one pass.
'''

class Solution:
    def removeNthFromEnd_1(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        '''
        Accoring to the requirement. It asks us to do this in one pass.
        If it is not required to use only one pass, basically, there are three ways to implement this.


        1. n wide block (one pass)
            use n wide block and move the block. Once the righ markert hits the end of linked list,
            the left marker is the n-1 th node from the end of list.
            It needs two while/ for loop.

        2. the (L - n + 1)th node from the begining (two passes)
            Get the total number(length) of linked list, called L.
            The nth node from the end  = The (L - n + 1)th node from the head
            
        3. Reverse the linked list (two passes)
            Reverse the linked list, then remove the nth node from the head.
            Reverse linked list again.


        '''
        '''
        First create the dummy node in front head.
        The reason is that if n = 1, length of linked list is 1.
        After this method, the linked list should be none.

        '''

        dummy = ListNode(0)
        dummy.next = head
        left = dummy
        right = dummy

        #  get the n th node from head, stored in right marker
        count = 1
        for i in range(n):
            right = right.next


        #  move the n + 1 wide block together (block includig left node and right node)
        while right.next:
            left = left.next
            right = right.next

        #  now left is pointed to the (n + 1)th from the end

        # remove the left.next (nth node)
        left.next = left.next.next
        return head
