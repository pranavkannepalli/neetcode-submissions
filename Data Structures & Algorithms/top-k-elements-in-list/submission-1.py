class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            d[i] = d.get(i, 0) + 1

        s = list(sorted(d.keys(), key=lambda item: -d[item]))
        return s[:k]