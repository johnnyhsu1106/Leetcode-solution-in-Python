'''
Given a list of words and two words word1 and word2,
return the shortest distance between these two words in the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = “coding”, word2 = “practice”, return 3.
Given word1 = "makes", word2 = "coding", return 1.

Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.
'''
class Solution:
    # @param {string[]} words
    # @param {string} word1
    # @param {string} word2
    # @return {integer}
    def shortestDistance(self, words, word1, word2):
        '''
        idea:
        1. Use the build-in list method: list.index()....

            return abs(words.index(word1) - words.index(word2))

            However, it may be raise error,
            becasue it will return the index of first one element found in the list.
            For example:
            words = ["practice", "makes", "perfect", "coding", "makes"].
            Given word1 = "makes", word2 = "coding", return 1.
            words.index(word1) = 1
            words.index(word2) = 3
            return 2 instead of 1


        2. use the for loop to find the index for each word
        Then use abs to calculate the distance of two words
        '''
        distance = len(words)
        idx1 = None # index for word1 in words
        idx2 = None # index for word2 in words

        for i in range(len(words)):
            if words[i] == word1:
                idx1 = i
            if words[i] == word2:
                idx2 = i
            if idx1 is not None and idx2 is not None:
                distance = min(distance, abs(idx1-idx2))
        return distance

#
#
# def main():
#     s = Solution()
#     words = ["practice", "makes", "perfect", "coding", "makes"]
#     word1 = 'coding'
#     word2 = 'practice'
#     print(s.shortestDistance(words, word1, word2) == 3)
#
#     word1 = 'makes'
#     word2 = 'coding'
#     print(s.shortestDistance(words, word1, word2) == 1)
#
#
# if __name__ == '__main__':
#     main()
