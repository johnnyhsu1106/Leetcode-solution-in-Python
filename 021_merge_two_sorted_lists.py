'''
Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists.
for example:
[1,2,2,3] + [1,3] = [1,1,2,2,3,3]
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        '''
        Because the list is sorted, the way of merging two sorted list is like the Merge Sort.

        Create a node of linked list for output, for example, dummy = ListNode(0)
        It doesn't mattter what the dummy (node) is.
        dummy is used for marked the begining of the output.
        The reason why we have to create a dummy node in the begining of the linked list
        is that when we manipulat the nodes of linked lists, we can make sure that
        the first node won't change during the node manipulation.

        Then, compare the first node of each list, then pointer is pointed to the small one.
        Then move the node of the list with the smaller node and the node of current_node
        Until node of one of list is None
        Then connect the tail of current_node to the head of the list, which first node is not None.

        For example:


        l1: 1 -> 3
        l2: 2 -> 5

        current list: 0
        dummy: 0
        current node: 0

        Loop:
            loop 1:
            l1 node: 1 < l2 node: 2
            so current list: 0 -> 1

            # move the node
            l1 node: 3
            l2 node: 2
            current node: 1
            ====================================
            loop 2:
            l1 node: 3 > l2 node: 2
            current node: 0-> 1 -> 2

            # move the node
            l1 node: 3
            l2 node: 5
            current node: 2
            ====================================
            loop 3:
            current node 0-> 1 -> 2 -> 3

            # move the node
            l1 node: None
            l2 node: 5
            current node: 3

        exit the loop

        Then, connect he current node (3) to l2 first node (5)
        current.next = l2

        current: 0-> 1 -> 2 -> 3 -> 5

        # not return the dummy (0), return the dummy.next (1)
        return dummy.next


        '''

        current_node = ListNode(0)
        dummy = current_node
        while l1 and l2:
            if l1.val < l2.val:
                current_node.next = l1
                l1 = l1.next
            else:
                current_node.next = l2
                l2 = l2.next
            current_node = current_node.next

        if l1:
            current_node.next = l1
        else:
            current_node.next = l2

        return dummy.next
