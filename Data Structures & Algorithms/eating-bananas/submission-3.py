class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        def can_eat(k):
            hours_passed = 0

            for pile in piles:
                hours_passed += math.ceil(pile / k)

            return hours_passed <= h

        rv = right
        while left <= right:
            mid = left + ((right - left) // 2)

            if can_eat(mid):
                rv = mid
                right = mid - 1
            else:
                left = mid + 1

        return rv