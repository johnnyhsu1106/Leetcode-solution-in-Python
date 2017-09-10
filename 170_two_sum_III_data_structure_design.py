'''
Design and implement a TwoSum class. It should support the following operations: add and find.

add - Add the number to an internal data structure.
find - Find if there exists any pair of numbers which sum is equal to the value.

For example,

add(1); add(3); add(5);
find(4) -> true
find(7) -> false

'''

from collections import defaultdict

class TwoSum(object):

    def __init__(self):
        """
        initialize your data structure here
        idea:
        use the dictionary/ hash map to search the number is O(1)
        """
        self.lookup = defaultdict(int)

    def add(self, number):
        """
        Add the number to an internal data structure.
        :rtype: nothing
        """
        self.lookup[number] += 1
#

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for num1 in self.lookup:
            num2 = value - num1
            if num2 in self.lookup:
                if num1 == num2 and self.lookup[num1] == 1:
                    return False
                return True
        return False


# def main():
#     two_sum = TwoSum()
#     two_sum.add(1)
#     two_sum.add(2)
#     two_sum.add(5)
#     print(two_sum.find(3) == True)
#     print(two_sum.find(4) == False)
#     print(two_sum.find(5) == False)
#     print(two_sum.find(6) == True)
#     '''
#     add(1); add(3); add(5);
#     find(4) -> true
#     find(7) -> false
#     '''
#
#
# if __name__ == '__main__':
#     main()
