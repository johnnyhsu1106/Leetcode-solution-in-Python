'''
Remove all elements from a linked list of integers that have value val.

Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):

        return str(self.val)


    def insert(self, val):

        while self.next:
            self = self.next
        self.next = ListNode(val)


    def printLists(self):
        output = ''
        while self.next:
            output += self.__repr__() + '->'
            self = self.next
        output += self.__repr__()
        print(output)



class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """

        '''
        idea:
        Create a dummy node as the head of linked list.
        Because the node, which is going to be removed, might be the original head of linked list
        '''
        dummy = ListNode(float('inf'))
        dummy.next = head
        prev_node = dummy
        curr_node = head


        while curr_node:
            if curr_node.val == val:
                prev_node.next = curr_node.next
                #remove the current_node (prev_node is connected to the current node's next node)
            else: # move forward to the next node(update the prev_node and curr_node)
                prev_node = curr_node
            curr_node = curr_node.next
        return dummy.next



# def main():
#     head = ListNode(0)
#     head.insert(1)
#     head.insert(2)
#     head.insert(6)
#     head.insert(3)
#     head.insert(4)
#     head.insert(5)
#     head.insert(6)
#     head.printLists()
#
#
#     s = Solution()
#     s.removeElements(head, 6)
#     head.printLists()
#
#
# if __name__ == '__main__':
#     main()
