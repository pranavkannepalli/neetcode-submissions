class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [(self.euclidianDistance(point), point) for point in points]
        heapq.heapify(heap)

        ret = []
        for i in range(k):
            ret.append(heapq.heappop(heap)[1])
        return ret

    def euclidianDistance(self, point):
        return math.sqrt(point[0] ** 2 + point[1] ** 2)