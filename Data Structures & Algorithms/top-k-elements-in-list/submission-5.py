class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        freq = [[] for i in range(len(nums)+1)]

        for num in nums:
            counter[num] += 1
        for key , value in counter.items():
            freq[value].append(key)
        
        rv = []
        for i in range(len(freq)-1 , 0 , -1):
            for num in freq[i]:
                rv.append(num)
                if len(rv) == k:
                    return rv