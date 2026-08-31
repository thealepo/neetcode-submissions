class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        '''
        basically, return True if between indices i & j in range k
        there is a nums[i] == nums[j]
        '''
        if len(nums) < 1:
            return

        window = set()
        left = 0
        for right in range(len(nums)):
            if (right - left) > k:
                window.remove(nums[left])
                left += 1
            
            if nums[right] in window:
                return True

            window.add(nums[right])

        return False