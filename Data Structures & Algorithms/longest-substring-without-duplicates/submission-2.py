class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_set = set()
        left = 0
        rv = 0

        for right in range(len(s)):
            while s[right] in hash_set:
                hash_set.remove(s[left])
                left += 1
                
            hash_set.add(s[right])
            window = right - left + 1

            rv = max(rv , window)

        return rv