class Solution:
    def isValid(self, s: str) -> bool:
        l = []
        pairs = {")":"(", "}":"{", "]":"["}
        for i in s:
            if i not in pairs:
                l.append(i)
            else:
                if not l or l.pop() != pairs[i]:
                    return False

        return not l