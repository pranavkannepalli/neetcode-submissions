class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counts = [0] * 26
        active = [0] * 26
        left = 0
        right = 0

        for i in s1:
            counts[ord(i) - 97] += 1
        
        while right < len(s2):
            print(active, counts, s2[left], s2[right])
            if active == counts:
                return True

            else:
                if (right - left) <= len(s1) - 1:
                    active[ord(s2[right]) - 97] += 1
                    right += 1
                else:
                    active[ord(s2[left]) - 97] -= 1
                    left += 1
        return active == counts
