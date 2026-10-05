class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        seen = set()
        heap = [(0, 0)]  # (cost, point)
        total = 0
        while len(seen) < n:
            # print(heap)
            cost, u = heapq.heappop(heap)
            if u in seen:
                continue
            seen.add(u)
            total += cost
            ux, uy = points[u]
            for v in range(n):
                if v not in seen:
                    heapq.heappush(heap, (abs(ux - points[v][0]) + abs(uy - points[v][1]), v))
        return total