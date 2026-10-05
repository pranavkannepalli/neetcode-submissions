class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def dfs(curr, left):
            if len(left) == 0:
                res.append(curr.copy())
                return
            for i in range(1, len(left)+1):
                s, n = left[:i], left[i:]
                if self.palindrome(s):
                    curr.append(s)
                    dfs(curr, n)
                    curr.pop()
        dfs([], s)
        return res
    def palindrome(self, s:str) -> bool:
        return s == s[::-1]