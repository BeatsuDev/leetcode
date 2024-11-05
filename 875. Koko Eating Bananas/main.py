from typing import List
import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        slowest = 1
        fastest = max(piles)

        while slowest < fastest:
            new_speed = (slowest + fastest) // 2
            time = self.timeGivenSpeed(piles, new_speed)

            # Find the slowest speed where time is still <= h
            if time <= h:
                fastest = new_speed
            else:
                slowest = new_speed + 1

        return slowest

    def timeGivenSpeed(self, piles: List[int], speed: int) -> int:
        return sum(
            math.ceil(pile / speed)
            for pile in piles
        )
