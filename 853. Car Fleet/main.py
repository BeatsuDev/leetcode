from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), key=lambda x: x[0])

        fleets, longest_time = 0, 0
        for i in range(len(cars)-1, -1, -1):
            time_to_target = (target - cars[i][0]) / cars[i][1]
            if longest_time < time_to_target:
                fleets += 1
                longest_time = time_to_target

        return fleets
