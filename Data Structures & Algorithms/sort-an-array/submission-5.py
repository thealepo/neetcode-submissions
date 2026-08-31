class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(array , left , mid , right):
            L , R = array[left:mid+1] , array[mid+1:right+1]
            i , j , k = left , 0 , 0

            while j < len(L) and k < len(R):
                if L[j] <= R[k]:
                    array[i] = L[j]
                    j += 1
                else:
                    array[i] = R[k]
                    k += 1
                i += 1

            while j < len(L):
                array[i] = L[j]
                j += 1
                i += 1
            while k < len(R):
                array[i] = R[k]
                k += 1
                i += 1

        def merge_sort(array , left , right):
            if left >= right:
                return

            mid = (left + right) // 2
            merge_sort(array , left , mid)
            merge_sort(array , mid+1 , right)
            merge(array , left , mid , right)

        merge_sort(nums , 0 , len(nums)-1)
        return nums