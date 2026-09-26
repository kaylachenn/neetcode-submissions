class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        col = len(matrix[0])

        left = 0
        right = (rows * col) - 1

        while left <= right:
            mid = (left + right) // 2
            r = mid // col
            c = mid % col

            if matrix[r][c] == target:
                return True
            elif target > matrix[r][c]:
                left = mid + 1
            else:
                right = mid - 1
        return False

        