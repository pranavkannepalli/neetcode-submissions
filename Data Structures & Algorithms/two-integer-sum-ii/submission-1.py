class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 1
        right = len(numbers)

        while numbers[left - 1] + numbers[right - 1] != target and left < right:
            if numbers[left - 1] + numbers[right - 1] < target:
                left += 1
            elif numbers[left - 1] + numbers[right - 1] > target:
                right -= 1
            
        return [left, right]