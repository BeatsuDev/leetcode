from dataclasses import dataclass
from collections import defaultdict


@dataclass
class TimeStampedValue:
    value: str
    timestamp: int


class TimeMap:
    def __init__(self):
        self.values = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.values[key].append(TimeStampedValue(value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        vals = self.values[key]
        
        if len(vals) == 0 or timestamp < vals[0].timestamp:
            return ""

        left, right = 0, len(vals)-1

        while vals[right].timestamp > timestamp:
            middle = (left + right) // 2

            if middle == left:
                return vals[left].value

            if vals[middle].timestamp > timestamp:
                right = middle - 1
            else:
                left = middle

        return vals[right].value
