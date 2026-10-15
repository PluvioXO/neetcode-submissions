class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def dfs(x: int, y:int):
            if x == n and y == m:
                return 1
            if x == n+1 or y == m+1:
                return 0
            l = dfs(x+1, y)
            r = dfs(x, y+1)
            return l+r
        return dfs(1, 1)