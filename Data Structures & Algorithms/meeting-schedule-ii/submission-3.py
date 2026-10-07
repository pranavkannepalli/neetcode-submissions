import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda iv: iv.start)
        ends = []  # min-heap of end times of rooms in use

        for iv in intervals:
            if ends and ends[0] <= iv.start:
                heapq.heapreplace(ends, iv.end)  # reuse the room that frees earliest
            else:
                heapq.heappush(ends, iv.end)     # need a new room
        return len(ends)