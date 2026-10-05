class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0

        def dfs(x, y) -> int:
            #print(grid)
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
                return 0
            if grid[x][y] in [0, "x"]:
                return 0
            grid[x][y] = "x"
            total = 1
            for i in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                total += dfs(x + i[0], y + i[1])
            return total
        
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                area = dfs(x, y)
                maxArea = max(maxArea, area)
        
        return maxArea