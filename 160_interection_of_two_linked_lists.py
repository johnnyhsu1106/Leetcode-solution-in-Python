'''
Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗
B:     b1 → b2 → b3
begin to intersect at node c1.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return str(self.val)

    def print_all(self):
        output = ''
        while self.next:
            output += self.__repr__() + '->'
            self = self.next
        output += self.__repr__()
        print(output)

class Solution:
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        '''
        idea:
        A:          a1 → a2
                           ↘
                             c1 → c2 → c3
                           ↗
        B:     b1 → b2 → b3

        calculate the length of each linked list, n1 = 5, n2 =6
        try to make the length of the two linked liks to be equal
        (it means for the linked list with longer length, move the starting marker n2 - n1 step from head node)
        like A, starting marker: a1
        like B, starting marker: b2
        Finally, go through each node step by step, if node A is node B , return node A or node B

        '''
        #  calcuate the length of linked list A
        curr_node_A = headA
        length_A = 0
        while curr_node_A:
            length_A += 1
            curr_node_A = curr_node_A.next

        # calculate the length of linked list B
        curr_node_B = headB
        length_B = 0
        while curr_node_B:
            length_B += 1
            curr_node_B = curr_node_B.next

        marker_A = headA
        marker_B = headB


        if length_A > length_B:
            #  linked list A is the longer one and update the marker A
            i = 0
            while i < length_A - length_B and marker_A:
                marker_A = marker_A.next
                i += 1

        elif length_A < length_B:
            #  update the marker B
            i = 0
            while i < length_B - length_A and marker_B:
                marker_B = marker_B.next
                i += 1

        i = 0
        while i < min(length_A, length_B):
            if marker_A is marker_B:
                return marker_B
            marker_A = marker_A.next
            marker_B = marker_B.next
            i += 1
        return None
#
# def main():
#     '''
#     A:               2
#                        ↘
#                          3 → 4
#                        ↗
#     B:           1 → 2
#     '''
#     headA = ListNode(2)
#     headA.next = ListNode(3)
#     headA.next.next = ListNode(4)
#     headA.print_all()
#
#     headB = ListNode(1)
#     headB.next = ListNode(2)
#     headB.next.next = headA.next
#     headB.next.next.next = ListNode(4)
#     headB.print_all()
#
#     s = Solution()
#     print(s.getIntersectionNode(headA, headB))
#
#
# if __name__ == '__main__':
#     main()
