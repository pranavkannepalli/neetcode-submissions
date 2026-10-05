class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dig_to_letters = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        res = []

        def dfs(curr, left):
            if len(left) == 0:
                res.append(curr)
                return
            for i in dig_to_letters[left[0]]:
                dfs(curr + i, left[1:])
        if len(digits) > 0:
            dfs("", digits)
        return res
