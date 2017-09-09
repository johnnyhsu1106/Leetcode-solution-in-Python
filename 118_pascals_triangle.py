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
        n = 0, [[1]]
        n = 1, [[1],[1,1]]
        n = 2, [[1],[1,1],[1,2,1]]

        For each row (n = 0, 1, 2, ..., numRows-1)
             For each element in one row (i=0, 1, ..., n)

                The first element and the last element in the list must be 1
                The other element has the following relationship.
                ai(n) = ai-1(n-1) + ai(n-1), if i != 0 or j != n
                otherwise, a0 = 1 and an+1 = 1, if i=0 or i = n

                note: i is the index of each list, n is the row number
        '''


        output = []
        for n in range(numRows):
            output.append([]) # create a new row 
            for i in range(n+1):
                if i == 0 or i == n:
                    output[n].append(1)
                else:
                    output[n].append(output[n-1][i-1] + output[n-1][i])
        return output

# def main():
#     s = Solution()
#     print(s.generate(1))
#     print(s.generate(5))
#
# if __name__ == '__main__':
#     main()
