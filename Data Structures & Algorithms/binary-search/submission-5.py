class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left , right = 0 , len(nums) - 1

        while left <= right:
            mid = left + ((right - left) // 2)

            # [-1,0,2,4,6,8]
            #   l   m      r

            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid

        return -1
