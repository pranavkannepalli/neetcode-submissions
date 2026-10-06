class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        possible = [False] * (amount + 1)
        possible[-1] = True

        queue = [(0, amount)]

        while queue:
            #print(queue)
            c = heapq.heappop(queue)
            if c[1] == 0:
                return c[0]

            for i in coins:
                if c[1] - i >= 0 and not possible[c[1] - i]:
                    heapq.heappush(queue, ((c[0] + 1, c[1] - i)))
                    possible[c[1] - i] = True
        return -1