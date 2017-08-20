'''
You are playing the following Nim Game with your friend:
There is a heap of stones on the table, each time one of you take turns to remove 1 to 3 stones.
The one who removes the last stone will be the winner.
You will take the first turn to remove the stones.
Both of you are very clever and have optimal strategies for the game.
Write a function to determine whether you can win the game given the number of stones in the heap.
For example, if there are 4 stones in the heap,
then you will never win the game: no matter 1, 2, or 3 stones you remove,
the last stone will always be removed by your friend.
'''
class Solution:
    def nimGame(self, n):
        '''
        case 1: if n <= 3, win, True
        case 2: if n = 4,  lose, False
        case 3: if n = 5,  win (1,1)(1,2)(1,3) True
        case 4: if n = 6,  win (2,1) (2,2) (2,3) True
        case 5: if n = 7,  win (3,1), (3,2), (3,3) True
        case 6: if n = 8,  lose
        '''
        return n % 4 != 0

# def main():
#     s = Solution()
#     print(s.nim_game(7))
#
# if __name__ == '__main__':
#     main()
