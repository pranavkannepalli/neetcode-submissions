class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums)//2
        dp = [False] * (target + 1)

        for num1 in nums:
            if num1 <= target:
                new_dp = dp.copy()
                for num2, found in enumerate(dp):
                    if found and num1 + num2 <= target:
                        new_dp[num1 + num2] = True
                new_dp[num1] = True
                dp = new_dp

        return dp[-1] 


        
