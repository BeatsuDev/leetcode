from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1

        largest_number = max(height)
        largest = 0

        # While it is still possible to find a greater sum
        while (right-left)*largest_number > largest:
            area = min(height[left], height[right]) * (right - left)
            if area > largest:
                largest = area
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return largest
