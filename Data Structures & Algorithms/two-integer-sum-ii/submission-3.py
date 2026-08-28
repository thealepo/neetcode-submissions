class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left , right = 0 , len(numbers)-1

        while left < right:
            addition = numbers[left] + numbers[right]

            if addition < target:
                left += 1
            elif addition > target:
                right -= 1
            else:
                return [left+1 , right+1]

        return []