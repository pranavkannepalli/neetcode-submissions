class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # bfs inwards from outer O's until queue is exhausted then replace nonreachable Os with Xs
        capturable = [[True] * len(board[0]) for _ in range(len(board))]
        visited = [[False] * len(board[0]) for _ in range(len(board))]
        queue = collections.deque()

        for i in range(len(board)):
            for j in [0, len(board[0]) - 1]:
                if board[i][j] == 'O':
                    capturable[i][j] = False
                    queue.append([i, j])
        
        for i in [0, len(board) - 1]:
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    capturable[i][j] = False
                    queue.append([i, j])

        while queue:
            c = queue.popleft()
            visited[c[0]][c[1]] = True

            for d in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                newX = c[0] + d[0]
                newY = c[1] + d[1]
                if 0 <= newX < len(board) and 0 <= newY < len(board[0]) and board[newX][newY] == 'O' and not visited[newX][newY]:
                    capturable[newX][newY] = False
                    queue.append([newX, newY])
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O' and capturable[i][j]:
                    board[i][j] = 'X'
