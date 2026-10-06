class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i, num in enumerate(nums):
            m = 0
            for j in range(0, i + 1):
                if nums[j] < num:
                    m = max(m, dp[j])
            dp[i] = 1 + m
        print(dp)
        return max(dp)