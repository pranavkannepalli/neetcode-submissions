class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ## bfs from each point inwards to find where you can visit from each border

        p = [[False] * len(heights[0]) for _ in range(len(heights))]
        a = [[False] * len(heights[0]) for _ in range(len(heights))]
        p_visited = [[False] * len(heights[0]) for _ in range(len(heights))]
        a_visited = [[False] * len(heights[0]) for _ in range(len(heights))]
        p_queue = collections.deque()
        a_queue = collections.deque()

        for i in range(len(heights)):
            p[i][0] = True
            a[i][len(heights[0]) - 1] = True
            p_queue.append([i, 0])
            a_queue.append([i, len(heights[0]) - 1])
        
        for i in range(len(heights[0])):
            p[0][i] = True
            a[len(heights) - 1][i] = True
            p_queue.append([0, i])
            a_queue.append([len(heights) - 1, i])

        while p_queue:
            curr = p_queue.popleft()
            # print(curr)
            # check all directions
            for d in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                if 0 <= curr[0] + d[0] < len(heights) and 0 <= curr[1] + d[1] < len(heights[0]):
                    if not p_visited[curr[0] + d[0]][curr[1] + d[1]] and heights[curr[0]][curr[1]] <= heights[curr[0] + d[0]][curr[1] + d[1]]:
                        p[curr[0] + d[0]][curr[1] + d[1]] = True
                        p_queue.append([curr[0] + d[0], curr[1] + d[1]])
                        p_visited[curr[0]][curr[1]] = True
        
        while a_queue:
            curr = a_queue.popleft()
            # check all directions
            for d in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                if 0 <= curr[0] + d[0] < len(heights) and 0 <= curr[1] + d[1] < len(heights[0]):
                    if not a_visited[curr[0] + d[0]][curr[1] + d[1]] and heights[curr[0]][curr[1]] <= heights[curr[0] + d[0]][curr[1] + d[1]]:
                        a[curr[0] + d[0]][curr[1] + d[1]] = True
                        a_queue.append([curr[0] + d[0], curr[1] + d[1]])
                        a_visited[curr[0]][curr[1]] = True
        #print(a, p)
        res = []
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if p[i][j] and a[i][j]:
                    res.append([i, j])
        return res