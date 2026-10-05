class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        inf = 2147483647
        m = len(grid)
        n = len(grid[0])
        q = deque()
        landCell = False
    
        for i in range(m):
            for j in range(n):
                if grid[i][j]==inf:
                    landCell = True
                if grid[i][j]==0:
                    q.append((i, j, 0))
        
        if not landCell or not q:
            return 
        
        while q:
            x, y, h = q.popleft()
            if x-1>=0 and grid[x-1][y]==inf:
                grid[x-1][y] = h+1
                q.append((x-1, y, h+1))
            if y-1>=0 and grid[x][y-1]==inf:
                grid[x][y-1] = h+1
                q.append((x, y-1, h+1))
            if x+1<m and grid[x+1][y]==inf:
                grid[x+1][y] = h+1
                q.append((x+1, y, h+1))
            if y+1<n and grid[x][y+1]==inf:
                grid[x][y+1] = h+1
                q.append((x, y+1, h+1))



        