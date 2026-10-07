class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        out = 0
        for i in range(len(num1)):
            for j in range(len(num2)):
                out += 10 ** (i + j) * int(num1[len(num1) - i - 1]) * int(num2[len(num2) - j - 1])
        return str(out)