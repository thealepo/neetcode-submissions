class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1_ptr , word2_ptr = 0 , 0
        rv = ''
        tick = True

        while word1_ptr < len(word1) and word2_ptr < len(word2):
            if tick:
                rv += word1[word1_ptr]
                word1_ptr += 1
                tick = False
            else:
                rv += word2[word2_ptr]
                word2_ptr += 1
                tick = True

        while word1_ptr < len(word1):
            rv += word1[word1_ptr]
            word1_ptr += 1
        while word2_ptr < len(word2):
            rv += word2[word2_ptr]
            word2_ptr += 1

        return rv