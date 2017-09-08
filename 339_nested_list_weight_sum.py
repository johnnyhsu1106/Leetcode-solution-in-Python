'''
Given a nested list of integers, return the sum of all integers in the list weighted by their depth.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Example 1:
Given the list [[1,1],2,[1,1]], return 10. (four 1's at depth 2, one 2 at depth 1)

Example 2:
Given the list [1,[4,[6]]], return 27.
(one 1 at depth 1, one 4 at depth 2, and one 6 at depth 3; 1 + 4*2 + 6*3 = 27)
'''

# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# class NestedInteger:
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSum_1(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        '''
        idea:
        1. Solve this problem by calling method recursively
        2. Solve this proble by using while loop and queue
        '''

        return depthSumHelper(nestedList, 1)

    def depthSumHelper(nestedList, depth):
        result = 0
        for element in nestedList:
            if element.isInteger():
                result += element.getInteger * depth
            else:
                result += depthSumHelper(element.getList, depth +1)
        return result



    def depthSum_2(self, nestedList):
        if len(nestedList) == 0:
            return 0

        queue = []
        result = 0
        # for all element in the first level, add (element, depth) into queue
        for element in nestedList:
            queue.append((element, 1))

        while queue:
            element, depth = quque.pop(0)
            if element.isInteger()
                result += element.getInteger * depth
            else:
                for inside_element in element.getList():
                    queue.append((inside_element, depth +1))
        return result
