class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        seen = [False] * (len(s) + 1)
        queue = collections.deque()
        queue.append(0)

        while queue:
            curr = queue.popleft()
            
            for i in wordDict:
                if curr + len(i) <= len(s) and not seen[curr + len(i)] and s[curr:curr+len(i)] == i:
                    queue.append(curr + len(i))
                    seen[curr + len(i)] = True
                    if curr + len(i) == len(s):
                        return True
        
        return False
        