class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        rv = float('inf')
        left = 0
        total = 0

        for right in range(len(nums)):
            total += nums[right]
            while total >= target:
                window = right - left + 1
                rv = min(rv, window)
                total -= nums[left]
                left += 1

        if rv == float('inf'):
            return 0
        else:
            return rv