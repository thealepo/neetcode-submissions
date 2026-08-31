class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ptr = len(nums1) - n
        i = 0
        while ptr < len(nums1):
            nums1[ptr] = nums2[i]
            ptr += 1
            i += 1
        nums1.sort()