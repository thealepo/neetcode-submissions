class Solution:
    def findMin(self, nums: List[int]) -> int:
        left , right = 0 , len(nums)-1
        rv = nums[0]

        while left <= right:
            if nums[left] < nums[right]:
                rv = min(rv , nums[left])
                break

            mid = left + ((right - left) // 2)
            rv = min(rv , nums[mid])
            if nums[mid] >= nums[left]:
                left = mid+1
            else:
                right = mid-1

        return rv
