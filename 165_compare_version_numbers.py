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
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        # while i < len(version1) or j < len(version2):
        i = 0
        v1 = 0
        while i < len(version1) and version1[i] != '.':
            v1 = v1  *10 + version1[i]
            i +=1

        i = 0
        v2 = 0
        while i < len(version2) and version2[i] != '.':
            v2 = v2  *10 + version2[i]
            i +=1
        if v1 > v2:
            return 1
        elif v1 < v2:
            return -1
        else:
            return 0
