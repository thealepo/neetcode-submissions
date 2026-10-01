class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        rv = 0

        for right in range(1, len(prices)):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                rv = max(rv, profit)
            else:
                left = right

            right += 1

        return rv