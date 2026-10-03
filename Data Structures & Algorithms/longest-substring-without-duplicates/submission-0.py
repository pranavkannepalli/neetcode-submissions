class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = {}
        maxlen = 0
        left = 0

        for i, c in enumerate(s):
            # print(c, chars)
            if c in chars:
                pos = chars[c]
                while left <= pos:
                    chars.pop(s[left], None)
                    left += 1
            chars[c] = i
            maxlen = max(maxlen, i - left + 1)
        return maxlen
