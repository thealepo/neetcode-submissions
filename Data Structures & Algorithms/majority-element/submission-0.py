class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = defaultdict(int)
        rv = max_count = 0

        for num in nums:
            counter[num] += 1
            if max_count < counter[num]:
                rv = num
                max_count = counter[num]
        return rv