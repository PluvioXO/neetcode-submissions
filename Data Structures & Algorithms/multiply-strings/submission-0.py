class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        ans = 0 
        def multiplyToPower(a, b) -> int:
            return a * int(b)

        i = len(num1)-1
        for o in num1:
            ans += multiplyToPower(int(o) * 10**i, num2)
            i -= 1
        return str(ans) 
        