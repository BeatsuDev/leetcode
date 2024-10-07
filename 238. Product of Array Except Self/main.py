from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)

        prefix_product = 1
        for i in range(len(nums)):
            output[i] = prefix_product
            prefix_product *= nums[i]

        postfix_product = 1
        for i in range(len(nums)):
            output[-1-i] *= postfix_product
            postfix_product *= nums[-1-i]

        return output
