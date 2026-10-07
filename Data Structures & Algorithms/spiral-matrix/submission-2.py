class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        d = 0
        res = []
        while matrix:
            print(matrix)
            if d == 0:
                res += matrix[0]
                matrix = matrix[1:]
            if d == 1:
                for i in matrix:
                    if len(i) > 0:
                        res.append(i.pop())
            if d == 2:
                r = matrix.pop()
                r.reverse()
                res += r
            if d == 3:
                for i in range(len(matrix) - 1, -1, -1):
                    if len(matrix[i]) > 0:
                        res.append(matrix[i][0])
                    matrix[i] = matrix[i][1:]
            d = (d + 1) % 4

        return res