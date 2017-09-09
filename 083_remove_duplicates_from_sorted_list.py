'''
Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return str(self.val)


class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        output = ''
        current_node = self.head
        while current_node.next:
            output += current_node.__repr__() + '->'
            current_node = current_node.next
        output += current_node.__repr__()
        return output

    def append(self, value):
        node = ListNode(value)
        if not self.head:
            self.head = node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = node



class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        '''
        Time: O(n)
        Space: O(1)
        
        current_node = head
        while
        start with current_node
            while
                find the next_node and check whether next_node exists and is equal to current_node
                if next_node is equal to current_node, find the next node
                until the node's value is not equal to current_node
            Assign the pointer to the node we find, whose value is not equal to current_node's value
            Then, move on  (current_node = next_node)

            Please see the problem 026

            PS: the whole idea is like remove dulplicates element from a sorted array/list
            a sorted list, lst = [1,1,2,3,3]
            #  use two pointer
            i = 0
            j = 1
            output = [lst[0]]
            while i < len(lst):
                next_ele = lst[j]
                while j < len(lst) and lst[i] == lst[j]:
                    j += 1
                output.appnd(lst[j])
                i = j
            return output
        '''
        current_node = head

        while current_node:
            next_node = current_node.next
            while next_node and next_node.val == current_node.val:
                next_node = next_node.next
            current_node.next = next_node

            current_node = next_node
        return head


# def main():
#
#     #  Test Case 1
#     linked_list = LinkedList()
#     linked_list.append(1)
#     linked_list.append(1)
#     linked_list.append(2)
#     print(linked_list)
#
#     s = Solution()
#     s.deleteDuplicates(linked_list.head)
#     print(linked_list)
#
#
#     # Test case 2
#     linked_list = LinkedList()
#     linked_list.append(1)
#     linked_list.append(1)
#     linked_list.append(2)
#     linked_list.append(3)
#     linked_list.append(3)
#
#     print(linked_list)
#
#     s = Solution()
#     s.deleteDuplicates(linked_list.head)
#     print(linked_list)
#
# if __name__ == '__main__':
#     main()
