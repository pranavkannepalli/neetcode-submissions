class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        suffix = [1]
        l = len(nums)

        for i in range(l):
            prefix.append(prefix[-1] * nums[i])
            suffix.append(suffix[-1] * nums[l - i - 1])
        suffix.reverse()
        out = []
        for i in range(l):
            out.append(prefix[i] * suffix[i + 1])
        return out