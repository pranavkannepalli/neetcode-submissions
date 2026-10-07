"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda interval:-interval.start)
        heap = []


        while intervals:
            n = intervals.pop()
            if len(heap) > 0 and n.start >= heap[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, n.end)
            
        return len(heap)