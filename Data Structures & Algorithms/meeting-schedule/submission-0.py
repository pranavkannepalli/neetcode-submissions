"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key= lambda interval: interval.start)
        curr = 0

        while curr < len(intervals) - 1:
            c = intervals[curr]
            n = intervals[curr + 1]

            if c.end > n.start:
                return False
            curr += 1
        return True