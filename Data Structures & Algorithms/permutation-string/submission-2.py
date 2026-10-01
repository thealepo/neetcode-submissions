from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        dict_s1 = defaultdict(int)
        for c in s1:
            dict_s1[c] += 1

        # check in s2
        dict_s2 = defaultdict(int)
        left, i = 0, 0
        while i < len(s1):
            dict_s2[s2[i]] += 1
            i += 1

        for right in range(i, len(s2)):
            if dict_s1 == dict_s2:
                return True

            dict_s2[s2[left]] -= 1
            if dict_s2[s2[left]] == 0:
                del dict_s2[s2[left]]
            left += 1

            dict_s2[s2[right]] += 1
            
        return dict_s1 == dict_s2
        


