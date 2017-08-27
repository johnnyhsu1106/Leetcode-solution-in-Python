'''
Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.
Notes:
You must use only standard operations of a queue --
which means only push to back, peek/pop from front, size, and is empty operations are valid.
Depending on your language, queue may not be supported natively.
You may simulate a queue by using a list or deque (double-ended queue),
as long as you use only standard operations of a queue.
You may assume that all operations are valid
(for example, no pop or top operations will be called on an empty stack).
'''

class Queue:
    '''
    Consider using the build-in data type List to implement Queue
    '''
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if not self.empty():
            return self.items.pop(0)


    def peek(self):
        if not self.empty():
            return self.items[0]

    def size(self):
        return len(self.items)

    def empty(self):
        return len(self.items) == 0
    def __repr__(self):
        output = '['
        for i in range(self.size()):
            output += str(self.items[i])
        output += ']'
        return output



class MyStack:
    '''
    idea:
    use only 1 Queue to implement the Stack.
    queue = [1,2,3,4,5], n = 5

    1. stack.pop(): it should return 1....
        The way we should do is to shift (pop-push) the n-1 element from the begining to the end
        so queue = [5,1,2,3,4] then pop the first one element.
    2. stack.push(6): just use queue.push(6)
        queue = [1,2,3,4,5,6]
    3. top
        like  stack.pop(), we shift n-1 element from the begining to the end. Then peek the first element.
        queue = [6,1,2,3,4,5]
        Then, one more shift, so the queue = [1,2,3,4,5,6]
    '''
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = Queue()

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.queue.push(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        for i in range(self.queue.size() -1):
            self.queue.push(self.queue.pop())
        return self.queue.pop()

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        for i in range(self.queue.size() -1):
            self.queue.push(self.queue.pop())
        top_element = self.queue.peek()
        self.queue.push(self.queue.pop())
        return top_element


    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return self.queue.empty()


#
# def main():
#     stack = MyStack()
#     stack.push(1)
#     print(stack.top() == 1)
#     print(stack.pop() == 1)
#     print(stack.empty() == True)
#
#
# if __name__ == '__main__':
#     main()
