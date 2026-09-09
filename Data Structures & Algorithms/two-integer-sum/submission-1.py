class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_index = {}
        for i, val in enumerate(nums):
            if val in diff_index.keys():
                return [diff_index[val], i]
            else:
                diff_index[target - val] = i