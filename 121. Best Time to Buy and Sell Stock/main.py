from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        best = 0
        for price in prices[1:]:
            if price < lowest:
                lowest = price
            elif price - lowest > best:
                best = price-lowest

        return best
