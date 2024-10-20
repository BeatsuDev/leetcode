from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        return self.recursive_solver(n, 0, 0)

    def recursive_solver(self, n: int, openings_used: int, closes_used: int) -> List[str]:
        if openings_used == n:
            return [")"*(n-closes_used)]

        outputs = [
            "("+s
            for s in self.recursive_solver(n, openings_used+1, closes_used)
        ]

        if closes_used < openings_used:
            outputs.extend([
                ")"+s
                for s in self.recursive_solver(n, openings_used, closes_used+1)
            ])

        return outputs
