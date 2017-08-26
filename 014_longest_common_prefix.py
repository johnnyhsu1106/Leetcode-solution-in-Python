'''
Write a function to find the longest common prefix string amongst an array of strings.
'''
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        '''
        find the longest common prefix amongst all elements
        For example:
        ["hello", "heal", "heavy"] -> return he

        idea:
        pick any string in the array.
        check each char from the beginng of this string and other's.
        For exapmle:
        pick the first string in the array(strs[0]), 'hello'

        compare this with the rest of stings in the array  ["heal", "heavy"]
        if any char from the begining in the ["heal", "heavy"] is not matching the any char from the beging of "hello"
        return the index, or index > len("heal") -1 return strs[0][0:i]
        if it is matching, return strs[0]
        '''

        # edge case
        if len(strs) == 0:
            return ''


        for i in range(len(strs[0])):
            for string in strs[1:]:
                if strs[0][i] != string[i] or i >= len(string):
                    return strs[0][0:i]
        return strs[0]


# def main():
#     s = Solution()
#     print(s.longestCommonPrefix(["healo", "heal", "heavy"]))
#
# if __name__ == '__main__':
#     main()
