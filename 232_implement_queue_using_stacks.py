'''
Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.

Notes:
You must use only standard operations of a stack --
which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, stack may not be supported natively.
You may simulate a stack by using a list or deque (double-ended queue),
as long as you use only standard operations of a stack.
You may assume that all operations are valid (for example,
no pop or peek operations will be called on an empty queue).
'''
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Stack_node:
    def __init__(self):
        self.top = None

    def push(self, val):
        node = Node(val)
        if self.top:
            node.next = self.top
            self.top = node
        else:
            self.top = node

    def pop(self):
        if self.top:
            node = self.top
            self.top = node.next
            return node.val
        return None

    def empty(self):
        return self.top is None

    def peek(self):
        return self.top.val


class Stack_list:
    def __init__(self):
        self.values = []

    def push(self, value):
        self.values.append(value)

    def pop(self):
        if not self.empty():
            return self.values.pop()

    def peek(self):
        if not self.empty():
            return self.values[-1]

    def empty(self):
        return len(self.values) == 0

class MyQueue:
    '''
    First, define the class Stack above.
    Then implement the stack method: push(), pop(), peek(), empty()
    There are two way to implement Stack:
    1. Create Node class
    2. Use build-in data structure - list

    idea:
    Use two stacks to implement the queue.
    One stack called old_stack keeps the oldest element on the top
    Another stack called new_stack keeps the latest element on the top

    Push these element 1, 2, 3, 4, 5, 6, 7, 8

    old_stack       new_stack
        1
        2
        3               8
        4               7
        5               6

    '''


    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.old_stack = Stack_list()
        self.new_stack = Stack_list()


    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        '''
        idea:
        Push the element into new_stack
        '''
        self.new_stack.push(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """

        '''
        Pop element from old_stack.
        Before pop element x from old_stack, make sure old_stack is not empty.
        If old_stack is empty, add all elements in new_stack to old_stack
        '''
        self._shift_stacks()
        return self.old_stack.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        '''
        Before peek element x from old_stack, make sure old_stack is not empty.
        If old_stack is empty, add all elements in new_stack to old_stack
        '''
        self._shift_stacks()
        return self.old_stack.peek()


    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return self.old_stack.empty() and self.new_stack.empty()


    def _shift_stacks(self):
        '''
        This is a private method for shifting all elements from new_stack to old_stack
        if old_stack is empty.
        '''
        if self.old_stack.empty():
            while not self.new_stack.empty():
                self.old_stack.push(self.new_stack.pop())




def main():
    #  Test the class Stack
    stack = Stack_node()
    print(stack.empty() == True)
    stack.push(1)
    stack.push(2)
    print(stack.peek() == 2)
    print(stack.pop() == 2)
    print(stack.pop() == 1)
    print(stack.empty() == True)


    #  Test the class MyQueue
    queue = MyQueue()
    queue.push(1)
    queue.push(2)
    print(queue.peek() == 1)
    print(queue.pop() == 1)



if __name__ == '__main__':
    main()
