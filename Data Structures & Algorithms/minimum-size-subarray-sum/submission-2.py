class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        total = 0
        rv = float('inf')

        for right in range(len(nums)):
            total += nums[right]

            while total >= target:
                rv = min(rv , right - left + 1)
                total -= nums[left]
                left += 1

        return 0 if rv == float('inf') else rv