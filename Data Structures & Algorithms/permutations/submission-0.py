class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(curr, left):
            if len(left) == 0:
                res.append(curr.copy())
                return
            for i in left:
                l = [j for j in left if j != i]
                curr.append(i)
                dfs(curr, l)
                curr.pop()
        dfs([], nums)
        return res