'''
Given a string, we can "shift" each of its letter to its successive letter,
for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:

"abc" -> "bcd" -> ... -> "xyz"
Given a list of strings which contains only lowercase alphabets,
group all strings that belong to the same shifting sequence.

For example, given: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
Return:

[
  ["abc","bcd","xyz"],
  ["az","ba"],
  ["acef"],
  ["a","z"]
]

Note: For the return value, each inner list's elements must follow the lexicographic order.
'''
from collections import defaultdict
class Solution:
    # @param {string[]} strings
    # @return {string[][]}
    def groupStrings(self, strings):
        groups = defaultdict(list)
        for s in strings:
            groups[self.hash_str(s)].append(s)

        result = []
        for key in groups:
            result.append(sorted(groups[key]))
        return result

    def hash_str(self, s):
        hashcode = ''
        base = ord(s[0])
        for char in s:
            if ord(char) - base >= 0:
                hashcode += chr(ord('a')+ ord(char) - base)
            else:
                hashcode += chr(ord('a')+ ord(char) - base + 26)
        return hashcode


# def main():
#     s = Solution()
    # print(s.hash_str('cba'))
    # print(s.hash_str('baz'))

#     print(s.groupStrings(["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]))
#
# if __name__ == '__main__':
#     main()
