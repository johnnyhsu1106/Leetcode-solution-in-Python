'''
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).
Write a function to determine if a number is strobogrammatic.
The number is represented as a string.
For example, the numbers "69", "88", and "818" are all strobogrammatic.


Hints:
two pointers
'''
class Solution:

    # @param {string} num
    # @return {boolean}
    def isStrobogrammatic(self, num):
        '''
        idea:
        create a dictionary/map to look up.
        use two pointers to fetch the values of two pointers.

        '''
        stro_num = {'0':'0', '1':'1','6':'9', '8':'8', '9':'6'}
        start = 0
        end = len(num)-1
        while start < end:
            if num[start] not in stro_num or num[end] not in stro_num:
                return False
            elif stro_num[num[start]] != num[end] or stro_num[num[end]] != num[start]:
                return False
            start += 1
            end -= 1
        return True


#
# def main():
#     s = Solution()
#     print(s.isStrobogrammatic('123'))
#     print(s.isStrobogrammatic('801'))
#     print(s.isStrobogrammatic('808'))
#     print(s.isStrobogrammatic('69'))
#     print(s.isStrobogrammatic('1001'))
#
#
# if __name__ == '__main__':
#     main()
