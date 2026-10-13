class Solution:
    def longestPalindrome(self, s: str) -> str:
        rv_idx, rv_len = 0, 0
        n = len(s)

        for i in range(n):
            # Odd length
            left, right = i, i
            while left >= 0 and right < n and s[left] == s[right]:
                if (right - left + 1) > rv_len:
                    rv_idx = left
                    rv_len = right - left + 1
                left -= 1
                right += 1

            # Even length
            left, right = i, i + 1
            while left >= 0 and right < n and s[left] == s[right]:
                if (right - left + 1) > rv_len:
                    rv_idx = left
                    rv_len = right - left + 1
                left -= 1
                right += 1

        return s[rv_idx : rv_idx + rv_len]