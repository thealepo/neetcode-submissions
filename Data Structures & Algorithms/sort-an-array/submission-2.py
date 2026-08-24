class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr , left , mid , right):
            L , R = arr[left:mid+1] , arr[mid+1:right+1]
            i , j , k = left , 0 , 0

            while j < len(L) and k < len(R):
                if L[j] <= R[k]:
                    arr[i] = L[j]
                    j += 1
                else:
                    arr[i] = R[k]
                    k += 1
                i += 1

            while j < len(L):
                arr[i] = L[j]
                j += 1
                i += 1
            while k < len(R):
                arr[i] = R[k]
                k += 1
                i += 1

        def merge_sort(arr , left , right):
            if left >= right:
                return
            mid = (left + right) // 2
            merge_sort(arr , left , mid)
            merge_sort(arr , mid+1 , right)
            merge(arr , left , mid , right)

        merge_sort(nums , 0 , len(nums)-1)
        return nums