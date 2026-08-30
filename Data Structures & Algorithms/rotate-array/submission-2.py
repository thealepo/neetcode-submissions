class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n

        def reverse(left , right):
            while left < right:
                nums[left] , nums[right] = nums[right] , nums[left]
                left += 1
                right -= 1

        # [1,2,3,4,5] , k=2
        reverse(0 , n-1)  # rotate the whole array: [5,4,3,2,1]
        reverse(0 , k-1)  # rotate first k elements:  [4,5,3,2,1]
        reverse(k , n-1)  # rotate remaining elements: [4,5,1,2,3]