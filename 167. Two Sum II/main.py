from typing import List


# Time complexity: O(n)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers)-1

        while j > i:
            two_sum = numbers[i] + numbers[j]
            if two_sum > target:
                j -= 1
            elif two_sum < target:
                i += 1
            else:
                return i+1, j+1


# Time complexity: O(n log(n))
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        last_index = len(numbers)-1
        for i, n in enumerate(numbers):
            compliment_index = self.binary_search(numbers, i+1, last_index, target-n)
            if compliment_index > 0:
                return (i+1, compliment_index+1)
        
    def binary_search(self, numbers: List[int], start: int, end: int, target: int) -> int:
        if start == end:
            if numbers[start] == target:
                return start
            return -1
        
        middle = (end + start) // 2
        if target > numbers[middle]:
            return self.binary_search(numbers, middle+1, end, target)
        return self.binary_search(numbers, start, middle, target)
