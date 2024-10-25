from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            while len(stack) > 0 and temperatures[stack[-1]] < temp:
                index = stack.pop()
                output[index] = i - index

            stack.append(i)

        return output
