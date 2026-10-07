class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        first_col_zero = False

        # Pass 1: record markers in row 0 / col 0
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_zero = True
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0   # mark row i
                    matrix[0][j] = 0   # mark col j

        # Pass 2: fill the interior from the markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Pass 3: row 0 (matrix[0][0] is its marker)
        if matrix[0][0] == 0:
            for j in range(n):
                matrix[0][j] = 0

        # Pass 4: col 0
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0