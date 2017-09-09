'''
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

For example,
MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3
'''
class MovingAverage:
    '''
    idea:
    Use Queue to slove this problem.
    
    '''
    def __init__(self, size):
        self.size = size
        self.sum = 0
        self.queue = []

    def next(self, num):

        if len(self.queue) == self.size:
            self.sum -= self.queue.pop(0)
        self.sum += num
        self.queue.append(num)
        return self.sum / len(self.queue)

# def main():
#     m = MovingAverage(3)
#     print(m.next(1))
#     print(m.next(10))
#     print(m.next(3))
#     print(m.next(5))
#
#
# if __name__ == '__main__':
#     main()
