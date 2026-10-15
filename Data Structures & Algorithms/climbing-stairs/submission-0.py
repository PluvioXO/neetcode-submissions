class Solution:
    def climbStairs(self, n: int) -> int:
        def dp(a: int, num: int):
            if a - 1 == 0:
                num += 1
                return num;
            if a - 2 == 0: 
                num += 1
                return dp(a-1, num)
            else:
                return dp(a-2, num) + dp(a-1, num)
        return dp(n, 0)
 
