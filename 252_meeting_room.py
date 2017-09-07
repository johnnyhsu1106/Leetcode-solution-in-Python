'''
Given an array of meeting time intervals consisting of start
and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

For example,
Given [[0, 30],[5, 10],[15, 20]],
return false.
'''

class Solution:
    """
    input: List of List, List of [Intervals]
    output: Boolean
    """
    def canAttendMeetings(self, intervals):
        '''
        idea: if si < ej, (i != j) , return False
        '''
        intervals.sort()

        for i in range(0, len(intervals)-1):
            end_time = intervals[i][1]
            start_time = intervals[i+1][0]

            if start_time < end_time:
                return False
        return True
