from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_index = self.binary_search_row(matrix, target)
        return self.binary_search(matrix[row_index], target) >= 0

    def binary_search_row(self, matrix: List[List[int]], target: int) -> int:
        """Finds the row in which target may be in"""
        row_i, row_j = 0, len(matrix)-1

        while row_i < row_j:
            middle_index = (row_i + row_j) // 2
            if matrix[middle_index][0] > target:
                row_j = middle_index - 1
            elif  matrix[middle_index][-1] < target:
                row_i = middle_index + 1
            else:
                return middle_index
        return row_i if target >= matrix[row_i][0] and target <= matrix[row_i][-1] else -1

    def binary_search(self, array: List[int], target: int) -> int:
        i, j = 0, len(array)-1

        while i < j:
            middle = (i + j) // 2
            if array[middle] > target:
                j = middle - 1
            elif array[middle] < target:
                i = middle + 1
            else:
                return middle

        return i if array[i] == target else -1
