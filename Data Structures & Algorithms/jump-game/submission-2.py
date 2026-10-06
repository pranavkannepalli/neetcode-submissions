class Solution:
    def canJump(self, nums: List[int]) -> bool:
        visited = [False] * (len(nums))
        def dfs(ind):
            if ind == len(nums) - 1:
                return True
            else:
                visited[ind] = True
                for i in range(nums[ind], 0, -1):
                    if ind + i <= len(nums) - 1 and not visited[ind + i] and dfs(ind + i):
                        return True
            return False
        return dfs(0)