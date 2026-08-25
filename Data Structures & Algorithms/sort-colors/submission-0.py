class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = defaultdict(int)
        for col in nums:
            counter[col] += 1

        min_val , max_val = 0 , 2
        index = 0
        for col in range(0 , 3):
            while counter[col] > 0:
                nums[index] = col
                index += 1
                counter[col] -= 1