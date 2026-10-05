class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0

        def dfs(x, y):
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
                return
            if grid[x][y] == "0" or grid[x][y] == "x":
                return
            grid[x][y] = "x"
            dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            
            for i in dirs:
                dfs(x + i[0], y + i[1])
        
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == "0" or grid[x][y] == "x":
                    continue
                islands += 1
                dfs(x, y)
        
        return islands
