class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        seen = {}
        def dfs(x: int, y:int):
            if x == n and y == m:
                return 1
            if x == n+1 or y == m+1:
                return 0
            if f"{x},{y}" in seen:
                return seen[f"{x},{y}"]
            l = dfs(x+1, y)               
            r = dfs(x, y+1)
            seen[f'{x},{y}'] = l+r
            return l+r
        return dfs(1, 1)