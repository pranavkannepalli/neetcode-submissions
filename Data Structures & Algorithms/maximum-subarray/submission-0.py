class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = -float("infinity")
        curr = 0

        for i in nums:
            curr = curr + i
            maxSum = max(maxSum, curr)
            if curr < 0:
                curr = 0
            
        return maxSum