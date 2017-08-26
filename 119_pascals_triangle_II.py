'''
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].
Note:
Could you optimize your algorithm to use only O(k) extra space?
'''

class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        '''
                 [1]        k = 0
                [1,1]       k = 1
               [1,2,1]      k = 2
              [1,3,3,1]     k = 3
             [1,4,6,4,1]    k = 4

             aj(k) = aj-1(k-1) + aj(k-1), if j != 0 or j != k-1
             a0 = 1 and ak = 1, if j=0 or j = k-1

        '''
        prev_row = [1]

        if rowIndex == 0:
            return  prev_row

        for i in range(1,rowIndex+1): # for each row
            current_row = []
            for j in range(i+1): # for each element in each row
                if j == 0 or j == i:
                    current_row.append(1)
                else:
                    current_row.append(prev_row[j-1] + prev_row[j])
            prev_row = current_row # update the row (move on to the next row)

        return current_row

# def main():
#     s = Solution()
#     print(s.getRow(0))
#     print(s.getRow(1))
#     print(s.getRow(2))
#     print(s.getRow(3))
#
# if __name__ == '__main__':
#     main()
