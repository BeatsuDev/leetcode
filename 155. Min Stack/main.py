from typing import Tuple

class MinStack:
    def __init__(self):
        # First is stack value, second is min value
        # previously seen at the point in the stack
        self.stack: Tuple[int, int] = []

    @property
    def minimum(self) -> int:
        return self.stack[-1][1] if self.stack else 2**32 - 1

    def push(self, val: int) -> None:
        least = val if val < self.minimum else self.minimum
        self.stack.append((val, least))

    def pop(self) -> None:
        self.stack.pop()[0]

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
