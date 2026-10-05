class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def dfs(curr, left):
            if len(left) == 0:
                res.append(curr.copy())
                return
            curr.append(left[0])
            l = left[1:]
            dfs(curr, l)
            curr.pop()
            l = [i for i in left if i != left[0]]
            dfs(curr, l)
        
        dfs([], nums)
        return res