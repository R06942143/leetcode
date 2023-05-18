class Solution:
    def minimizeResult(self, expression: str) -> str:
        a, b = expression.split("+")

        ans = int(a) + int(b)
        ans_s = '(' + expression + ')'
        for i in range(len(a)):
            a1 = int(a[:i]) if i > 0 else 1
            a2 = int(a[i:])
            for j in range(len(b)):
                b1 = int(b[:j+1])
                b2 = int(b[j+1:]) if j + 1 < len(b) else 1
                t = a1 * (a2 + b1) * b2
                print(a1, a2, b1, b2, t)
                if t < ans:
                    ans = t
                    ans_s = ''
                    ans_s += a[:i] if i > 0 else ''
                    ans_s += '(' + a[i:] + '+' + b[:j+1] + ')'
                    ans_s += b[j+1:] if j + 1 < len(b) else ''
        return ans_s