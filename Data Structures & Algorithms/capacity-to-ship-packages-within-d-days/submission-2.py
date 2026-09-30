class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        rv = float('inf')

        def weight_capacity(capacity):
            ships, current_capacity = 1, capacity

            for w in weights:
                if current_capacity - w < 0:
                    ships += 1
                    if ships > days:
                        return False
                    current_capacity = capacity

                current_capacity -= w

            return True

        while left <= right:
            mid = left + ((right - left) // 2)

            if weight_capacity(mid):
                rv = min(rv, mid)
                right = mid - 1
            else:
                left = mid + 1

        return rv