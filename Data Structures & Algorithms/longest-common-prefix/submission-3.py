class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        rv = ''

        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or strs[0][i] != s[i]:
                    return rv
            rv += strs[0][i]

        return rv