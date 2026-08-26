'''
    [4 , 2 , 9 , 9 , 3 , 3 , 3 , 3] , k = 2  //  9,3

    counter = {2:1 , 3:4 , 4:1 , 9:2}
    buckets = [
        [2,4] , [9] , [] , [3] , [] , [] , [] , []
    ]

    rv = [3,9]

'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        buckets = [[] for _ in range(len(nums)+1)]

        for num in nums:
            counter[num] += 1
        for num , count in counter.items():
            buckets[count].append(num)

        rv = []
        for i in range(len(buckets)-1 , 0 , -1):
            for num in buckets[i]:
                rv.append(num)
                if len(rv) == k:
                    return rv
        