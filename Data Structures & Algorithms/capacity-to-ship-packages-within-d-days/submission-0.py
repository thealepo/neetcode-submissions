class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left , right = max(weights) , sum(weights)
        rv = right

        def can_ship(capacity):
            ships , curr_cap = 1 , capacity
            for w in weights:
                if curr_cap - w < 0:
                    ships += 1
                    curr_cap = capacity

                curr_cap -= w

            return ships <= days

        while left <= right:
            mid = left + ((right - left) // 2)

            if can_ship(mid):
                rv = min(rv , mid)
                right = mid - 1
            else:
                left = mid + 1

        return rv