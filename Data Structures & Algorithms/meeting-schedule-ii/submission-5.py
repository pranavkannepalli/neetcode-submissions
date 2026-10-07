"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0:
            return 0
        intervals.sort(key=lambda interval:-interval.start)
        heap = [intervals.pop().end]


        while intervals:
            n = intervals.pop()
            if n.start >= heap[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, n.end)
            
        return len(heap)