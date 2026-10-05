class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(x, y, curr) -> bool:
            if 0 > x  or x > len(board) - 1 or 0 > y or y > len(board[0]) - 1:
                return False
            if len(curr) == 1 and board[x][y] == curr[0]:
                return True
            if board[x][y] == curr[0]:
                temp = board[x][y]
                board[x][y] = ""
                for i in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                    if backtrack(x + i[0], y + i[1], curr[1:]):
                        return True
                board[x][y] = temp
                return False
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i, j, word):
                    return True
        return False