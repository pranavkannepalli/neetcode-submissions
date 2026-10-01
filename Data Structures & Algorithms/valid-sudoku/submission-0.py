class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        boxes = [[set() for i in range(3)] for i in range(3)]

        for i, row in enumerate(board):
            for j, val in enumerate(row):
                if val == ".":
                    continue
                if val in rows[i] or val in cols[j] or val in boxes[i // 3][j // 3]:
                    return False
                rows[i].add(val)
                cols[j].add(val)
                boxes[i // 3][j // 3].add(val)

        return True