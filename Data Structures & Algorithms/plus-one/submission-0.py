class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = [0] * (len(digits) + 1)
        carryover = True

        for i in range(len(digits) - 1, -1, -1):
            curr = digits[i] + (1 if carryover else 0)
            if curr == 10:
                curr = 0
                carryover = True
            else:
                carryover = False
            result[i + 1] = curr

        if carryover:
            result[0] = 1
            return result
        else:
            return result[1:] 