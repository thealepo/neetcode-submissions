class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # change nums in-place
        # return k
        k = len(nums)
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = float('inf')
                k -= 1

        nums.sort()
        return k