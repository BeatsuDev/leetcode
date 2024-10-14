
from typing import List, Tuple


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        solutions = []
        for i, a in enumerate(nums):
            if solutions and a == solutions[-1][0]:
                continue
            two_sum_solutions = self.two_sum(nums[i+1:], -a)
            
            if two_sum_solutions:
                for b, c in two_sum_solutions:
                    solutions.append([a, b, c])
        return solutions

    def two_sum(self, nums: List[int], target: int) -> List[Tuple[int, int]]:
        solutions = set()
        seen = set()
        for i, n in enumerate(nums):
            if target-n in seen:
                solutions.add((target-n, n))
            seen.add(n)
        return solutions