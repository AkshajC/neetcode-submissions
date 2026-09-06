class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        cur_min = max(prices)

        for elem in prices:
            maxProfit = max(elem - cur_min, maxProfit)
            cur_min = min(cur_min, elem)
        return maxProfit