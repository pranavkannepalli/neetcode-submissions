class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # m + n choose n

        return int(math.factorial(m + n - 2) / (math.factorial(n- 1) * math.factorial(m-1)))