class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [float("infinity")] * (len(nums))
        dp[0] = 0

        for i, maxJump in enumerate(nums):
            for jump in range(1, maxJump + 1):
                if i + jump < len(nums):
                    dp[i + jump] = min(dp[i] + 1, dp[i + jump])
        
        return dp[-1]