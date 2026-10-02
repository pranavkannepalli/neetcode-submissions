class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for i in tokens:
            match i:
                case '+':
                    a, b = s.pop(), s.pop()
                    s.append(a + b)
                case '-':
                    a, b = s.pop(), s.pop()
                    s.append(b - a)
                case '*':
                    a, b = s.pop(), s.pop()
                    s.append(a * b)
                case '/':
                    a, b = s.pop(), s.pop()
                    result = abs(b) // abs(a)
                    if (a < 0) != (b < 0):
                        result = -result
                    s.append(result)
                case _:
                    s.append(int(i))
        return s.pop()