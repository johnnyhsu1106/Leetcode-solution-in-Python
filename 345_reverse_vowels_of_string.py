'''
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".

Note:
The vowels does not include the letter "y".
'''

class Solution:

    def reverseVowels_1(self, s):
        """
        :type s: str
        :rtype: str
        """
        '''
        Transfer the string to list so we can manipulate each char easily.

        Idea 1 :
        Search the vowel in the list from the begining and from the end at the same time (backward/forward)
        Use two index, j and j, to track the location of vowels.
        swap the vowel using the i and j

        Idea 2:
        Use the list to store all locations of vowels in the list.
        swap the vowels based on the list, which stores all location of vowels.
        '''
        vowels = 'aeiou'
        string = list(s)
        i , j = 0, len(s)-1
        while i < j:
            # find the vowel from the begining
            if string[i].lower() not in vowels:
                i += 1

            # find the vowel from the end
            elif string[j].lower() not in vowels:
                j -= 1
            else:
                string[i], string[j] = string[j], string[i]
                i += 1
                j -= 1
        return ''.join(string)



    def reverseVowels_2(self, s):

        vowels = 'aeiouAEIOU'
        # store all positions of vowels
        position = []
        for i in range(len(s)):
            if s[i] in vowels:
                position.append(i)
        i = 0
        j = len(position)-1
        string = list(s)
        while i < j:
            # swap the the positin of vowel in the list
            string[position[i]], string[position[j]] = string[position[j]], string[position[i]]
            i += 1
            j -= 1
        # join all the element (char) in the list, turn into string
        return ''.join(string)




# def main():
#     s = Solution()
#     print(s.reverseVowels_1('Hello'))
#     print(s.reverseVowels_1('Aa'))
#
#
#     print(s.reverseVowels_2('Hello'))
#     print(s.reverseVowels_2('Aa'))
#
#
# if __name__ == '__main__':
#     main()
