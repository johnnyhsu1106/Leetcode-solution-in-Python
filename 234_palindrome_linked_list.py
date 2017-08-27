'''
Given a singly linked list, determine if it is a palindrome.

Follow up:
Could you do it in O(n) time and O(1) space?
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
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        '''
        idea: reverse the linked list and compare the corresponding node's vals
        1. Go through each node and fetch the value, concatate the value into string, called s1
        2. Reverse the linked list, repeat the step 1, and then get string s2.
        3. return s1 == s2
        '''
        s1 = self.fetchAllNodeValue(head)
        head = self.reverse(head)
        s2 = self.fetchAllNodeValue(head)
        return s1 == s2

    def fetchAllNodeValue(self, head):
        s1 = ''
        curr_node = head
        while curr_node:
            s1 += str(curr_node.val)
            curr_node = curr_node.next
        return s1



    def reverse(self, head):
        prev_node = None
        curr_node = head
        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        head = prev_node
        return head


# def main():
#     s = Solution()
#
#     head = ListNode(1)
#     head.next = ListNode(1)
#     head.next.next = ListNode(2)
#     head.next.next.next = ListNode(1)

    # head.print_all()
    # print(s.concatateAllNodeValue(head))
    #
    #
    # rev_head = s.reverse(head)
    # rev_head.print_all()
    # print(s.concatateAllNodeValue(rev_head))


    # print(s.isPalindrome(head))

# if __name__ == '__main__':
#     main()
