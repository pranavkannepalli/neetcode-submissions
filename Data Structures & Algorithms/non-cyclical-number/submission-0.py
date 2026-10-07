class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        visited.add(n)

        while n != 1:
            new = 0
            while n != 0:
                new += (n % 10) ** 2
                n = n // 10
            n = new
            if new in visited:
                return False
            else:
                visited.add(new)
        return True