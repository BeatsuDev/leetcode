from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen_quadrants = [set() for _ in range(9)]
        seen_columns = [set() for _ in range(9)]

        for i, row in enumerate(board):
            seen_row = set()
            for j, value in enumerate(row):
                if value == ".": continue

                if value in seen_row:
                    return False

                if value in seen_columns[j]:
                    return False

                quadrant = (i // 3) * 3 + j // 3
                if value in seen_quadrants[quadrant]:
                    return False

                seen_row.add(value)
                seen_columns[j].add(value)
                seen_quadrants[quadrant].add(value)
                
        return True