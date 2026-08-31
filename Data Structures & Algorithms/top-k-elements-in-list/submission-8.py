class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. create our data structures
        counter = defaultdict(int)
        freq = [[] for _ in range(len(nums)+1)]

        # 2. populate our structures
        # counter that tracks # of occurences per number
        # freq that tracks the numbers that appear `count` times
        for num in nums:
            counter[num] += 1
        for num , count in counter.items():
            freq[count].append(num)

        # 3. traverse list in reverse, append to rv until we reach
        # len(rv) == k
        rv = []
        for i in range(len(freq)-1 , 0 , -1):
            for num in freq[i]:
                rv.append(num)
                if len(rv) == k:
                    return rv