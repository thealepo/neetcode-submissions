from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = defaultdict(int)
        rv = 0

        left, max_freq = 0, 0
        for right in range(len(s)):
            counter[s[right]] += 1
            max_freq = max(max_freq, counter[s[right]])

            while (right - left + 1) - max_freq > k:
                counter[s[left]] -= 1
                left += 1

            rv = max(rv, right - left + 1)

        return rv