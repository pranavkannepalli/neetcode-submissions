class MedianFinder:

    def __init__(self):
        self.leftheap = []
        self.rightheap = []

    def addNum(self, num: int) -> None:
        # print(self.leftheap, self.rightheap)
        if len(self.leftheap) == 0:
            heapq.heappush_max(self.leftheap, num)
        elif num > self.leftheap[0]:
            heapq.heappush(self.rightheap, num)
            if len(self.rightheap) > len(self.leftheap):
                heapq.heappush_max(self.leftheap, heapq.heappop(self.rightheap))
        else:
            heapq.heappush_max(self.leftheap, num)
            if len(self.leftheap) > len(self.rightheap) + 1:
                heapq.heappush(self.rightheap, heapq.heappop_max(self.leftheap))

    def findMedian(self) -> float:
        if len(self.leftheap) == len(self.rightheap):
            return (self.leftheap[0] + self.rightheap[0]) / 2
        return self.leftheap[0]
        