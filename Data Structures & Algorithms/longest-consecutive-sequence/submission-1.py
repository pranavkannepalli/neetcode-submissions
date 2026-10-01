class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        m = 0
        for i in nums:
            if i - 1 in s:
                continue
            else:
                l = 1
                while i + l in s:
                    l += 1
                m = max(m, l)
        return m