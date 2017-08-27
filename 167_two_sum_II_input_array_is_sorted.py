'''
Given an array of integers that is already sorted in ascending order,
find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers
such that they add up to the target, where index1 must be less than index2.
Please note that your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
'''

class Solution:
    def twoSum_1(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        '''
        idea: please see the Problem 001
        Use a hashmap to track the number and its index plus 1.(key: vale = num: index +1)
        howerver, this algorithm is not using the codition 'input array is sorted'

        '''
        nums_map = {}
        for i in range(len(numbers)):
            num = numbers[i]
            value = target - num
            if value not in nums_map:
                nums_map[num] = i + 1
            else:
                return [nums_map[target - num], i+1]


    def twoSum_2(self, numbers, target):
        '''
        idea: brute force
        '''
        for i in range(len(numbers)):
            for j in range(i+1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i+1, j+1]

    def twoSum_3(self, numbers, target):
        '''
        idea:
        Because input array is sorted,
        we can get two number, numbers[start] and numbers[end] from the begining and the end,
        start is the index from the begining, start = 0, 1,...
        end is the index from the end, end = len(numbers)-1, len(numbers) -2,...
        if numbers[start] + numbers[end] < target, start ++
        elif numbers[start] + numbers[end] > target, end --
        elif numbers[start] + numbers[end] == target, return [start +1, end +1]
        '''

        start = 0
        end = len(numbers) -1
        while start < end:
            total = numbers[start] + numbers[end]
            if total < target:
                start += 1
            elif total > target:
                end -= 1
            else:
                return [start +1, end +1]


# def main():
#     s = Solution()
#     print(s.twoSum_1([2, 7, 11, 15],9) == [1,2])
#     print(s.twoSum_2([2, 7, 11, 15],9) == [1,2])
#     print(s.twoSum_3([2, 7, 11, 15],9) == [1,2])
#
# if __name__ == '__main__':
#     main()
