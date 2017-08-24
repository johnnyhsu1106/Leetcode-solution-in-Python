'''
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''
class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        '''
        idea:
        n = 1, [[1]]
        n = 2, [[1],[1,1]]
        n = 3, [[1],[1,1],[1,2,1]]

        For each row (i = 0, 1, 2, ..., n)
        For each element in one row (j=0, 1, ..., i)
        The first element and the last element in the list must be 1
        The other element has the following relationship.
        at n=k, aj = aj-1 + aj, at n=k-1, if j != 0 or j != k-1
        at n=k, a0 = 1 and ak = 1, if j=0 or j = k-1

        j is the index of each list, n is the row number
        '''


        output = []
        for i in range(numRows):
            output.append([])
            for j in range(i+1):
                if j == 0 or j == i:
                    output[i].append(1)
                else:
                    output[i].append(output[i-1][j-1] + output[i-1][j])
        return output
#
# def main():
#     s = Solution()
#     print(s.generate(1))
#     print(s.generate(5))
#
# if __name__ == '__main__':
#     main()
