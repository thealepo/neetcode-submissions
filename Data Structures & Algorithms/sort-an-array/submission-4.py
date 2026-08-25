class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def counting_sort():
            # step 1: count the occurences of each number
            # this is stored in a hashmap
            counter = defaultdict(int)
            for val in nums:
                counter[val] += 1
            
            # step 2: go in-order from least to greatest,
            # transferring the # of occurences per value
            min_val , max_val = min(nums) , max(nums)
            index = 0
            for val in range(min_val , max_val + 1):
                while counter[val] > 0:
                    nums[index] = val
                    index += 1
                    counter[val] -= 1

        counting_sort()
        return nums