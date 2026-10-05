class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or total > target or candidates[i] > target - total:
                return
            
            cur.append(candidates[i])
            dfs(i + 1, cur, total + candidates[i])
            cur.pop()
            curr_num = candidates[i]
            while i < len(candidates) and candidates[i] == curr_num:
                i += 1
            dfs(i, cur, total)
        dfs(0, [], 0)
        return res