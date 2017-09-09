'''
Compare two version numbers version1 and version2.
If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three",
it is the fifth second-level revision of the second first-level revision.

Here is an example of version numbers ordering:

0.1 < 1.1 < 1.2 < 13.37
'''
class Solution:
    def compareVersion_1(self, version1, version2):
        '''
        idea:
        Use the string.split() method to split the digits with '.'
        Then before comparing each corresponding element in each list,
        make sure two list with the same length by adding 0 to the shorter one.
        so 1.00 and 1 will be equal
        so 1.0 and 1.00 will be equal
        so 1.01 will bigger than 1
        '''
        v1 = [int(digit) for digit in version1.split('.')]
        v2 = [int(digit) for digit in version2.split('.')]

        while len(v1) != len(v2):
            if len(v1) > len(v2):
                v2.append(0)
            else:
                v1.append(0)
        for i in range(len(v1)):
            if v1[i] > v2[i]:
                return 1
            elif v1[i] < v2[i]:
                return -1
        return 0


    def compareVersion_2(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        '''
        idea:
        comparet each number, seperated by .
        '''
        v1_length = len(version1)
        v2_length = len(version2)
        i, j = 0, 0

        while i < v1_length or j < v2_length:

            v1, v2 = 0, 0
            while i < v1_length and version1[i] != '.':
                v1 = v1 * 10 + int(version1[i])
                i += 1
            while j < v2_length and version2[j] != '.':
                v2 = v2 * 10 + int(version2[j])
                j += 1
            print(v1,v2)
            if v1 != v2:
                if v1 > v2:
                    return 1
                else:
                    return -1
            i += 1
            j += 1

        return 0



# def main():
#     s = Solution()
#     version1 = '1.01'
#     version2 = '1.00.00'
#     print(s.compareVersion_1(version1,version2))
#     print(s.compareVersion_2(version1,version2))
#
#
#
# if __name__ == '__main__':
#     main()
