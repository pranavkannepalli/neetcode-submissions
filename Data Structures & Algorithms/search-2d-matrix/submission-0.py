class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix)-1
        row = (left + right) // 2

        # search for row
        while left <= right:
            if matrix[row][0] == target:
                return True
            elif matrix[row][0] > target:
                right = row - 1
            else:
                left = row + 1
            row = (left + right) // 2
        
        left = 0
        right = len(matrix[row])-1
        mid = (left + right) // 2

        # search for val in row
        while left <= right:
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                right = mid - 1
            else:
                left = mid + 1
            mid = (left + right) // 2

        return False