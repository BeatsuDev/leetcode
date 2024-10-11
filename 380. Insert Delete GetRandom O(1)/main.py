import random


class RandomizedSet:
    def __init__(self):
        self.index_map = {}
        self.array = []

    def insert(self, val: int) -> bool:
        if val in self.index_map: return False
        self.index_map[val] = len(self.array)
        self.array.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.index_map:
            return False

        if val == self.array[-1]:
            self.index_map.pop(val)
            self.array.pop()
            return True

        # Removing last element from list is O(1) time
        new_index = self.index_map.pop(val)
        self.index_map[self.array[-1]] = new_index
        self.array[new_index] = self.array.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.array)
