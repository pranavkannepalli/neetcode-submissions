class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda interval: -interval[0])
        res = [intervals.pop()]
        while len(intervals) != 0:
            # no intersect -> move forward
            # intersect -> merge and keep curr the same
            currInterval = res.pop()
            nextInterval = intervals.pop()
            # print(currInterval, nextInterval)
            if currInterval[1] >= nextInterval[0]:
                res.append([currInterval[0], max(currInterval[1], nextInterval[1])])
            else:
                res.append(currInterval)
                res.append(nextInterval)
        return res

            