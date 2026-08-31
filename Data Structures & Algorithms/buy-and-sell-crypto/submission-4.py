class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left , right = 0 , 1
        rv = 0

        for right in range(1 , len(prices)):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                rv = max(rv , profit)
            else:
                left = right
        
        return rv