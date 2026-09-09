class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) < len(s):
            s, t = t, s
        sl = {}
        for i in s:
            sl[i] = sl.get(i, 0) + 1
        
        for i in t:
            if i not in sl.keys() or sl[i] == 0:
                return False
            else:
                sl[i] = sl[i] - 1
        
        return True