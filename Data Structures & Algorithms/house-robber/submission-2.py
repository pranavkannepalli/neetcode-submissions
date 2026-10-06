class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        prev_if_take = nums[1]
        prev_if_leave = nums[0]

        for i in nums[2:]:
            temp = prev_if_take
            prev_if_take = prev_if_leave + i
            prev_if_leave = max(temp, prev_if_leave)


        return max(prev_if_take, prev_if_leave)