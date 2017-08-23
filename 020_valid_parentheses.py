'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
'''


'''
idea:
Use the stack to solve this problem
Scan the string from left to righ and every time we see the opening parentheses,
for example, '(', '[', '{'
we push it to stack because we want the last opening parentheses to be closed  first (FILO)

Then when wee see the closing parentheses,
we check whether the last opend parentheses is corresponding to the closing match,
by poping the element from stack. If it's a valid match, then we check next one, if not, return false.

At meantime, check if the stack is empty, return false.
It means there is no opening parentheses corresponding to the closing one.

In the end, after check all parentheses in the string, check if stack is empty or not.
If not empty, retun false. It the opening parentheses can't not match any closing parentheses.
'''

class Solution:
    def isValid_1(self, s):
        """
        :type s: str
        :rtype: bool
        """

        '''
        Use Python build-in List as Stack and
        build-in Dictionary as Hashtable (map) to lookup the open parethesis as key, closing parethesis as values
        '''
        #  edge case
        if len(s) % 2 == 1:
            return False


        stack = []
        # [].append() is equal to stack.push()
        # [].pop() is equal to stack.pop()
        # len([]) == 0 is equal to stack.empty()
        parentheses_map = {'(': ')', '[':']', '{': '}'}

        for char in s:
            # check the char is opening parethesis
            if char in parentheses_map:
                stack.append(char)
            else:
                if len(stack) == 0 or parentheses_map[stack.pop()] != char:
                    return False
        return len(stack) == 0



    def isValid_2(self, s):
        """
        :type s: str
        :rtype: bool
        """
        '''
        Create class Stack on your own.
        '''


        #  edge case:  the number of parentheses must be even , if string is valid parentheses
        if len(s) % 2 == 1:
            return False

        parentheses = [('(',')'), ('[',']'), ('{','}')]
        stack = Stack()

        for char in s:
            if self.open_parentheses(char, parentheses):
                stack.push(char)
            else:
                if stack.empty() or not self.match_parenthese(stack.pop(), char, parentheses):
                    return False

        return stack.empty()


    def open_parentheses(self,char, parentheses):
        '''
        This a a helper function to check whether the char is a opening parethesis
        '''
        for parentheses_pair in parentheses:
            if char == parentheses_pair[0]:
                return True
        return False
        

    def match_parenthese(self, opening_p, closing_p, parentheses):
        '''
        This a a helper function to check whether the opening parethesis and closing parethesis are match.
        '''
        for parentheses_pair in parentheses:
            if opening_p == parentheses_pair[0] and closing_p == parentheses_pair[1]:
                return True
        return False







class Stack:
    '''
    Use Python build-in data structure List to implement Stack.
    '''
    def __init__(self):
        self.values = []

    def push(self, value):
        self.values.append(value)

    def pop(self):
        if not self.empty():
            return self.values.pop()

    def empty(self):
        return len(self.values) == 0
