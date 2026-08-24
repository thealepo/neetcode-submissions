class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        counter = defaultdict(int)
        min_val , max_val = min(nums) , max(nums)
        for n in nums:
            counter[n] += 1
        
        i = 0
        for val in range(min_val , max_val + 1):
            while counter[val] > 0:
                nums[i] = val
                i += 1
                counter[val] -= 1

        return nums