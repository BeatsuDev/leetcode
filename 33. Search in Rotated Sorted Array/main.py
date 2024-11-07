from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1

        while left < right:
            middle = (left + right) // 2
            if nums[middle] == target: return middle

            start, end = nums[left], nums[middle]
            target_in_range = min(start, end) <= target < max(start, end)
            left_range_is_sorted = nums[left] <= nums[middle]

            # If it's sorted and in-range, or not sorted and out of range
            if left_range_is_sorted == target_in_range:
                right = middle - 1
            else:
                left = middle + 1

        return left if nums[left] == target else -1
