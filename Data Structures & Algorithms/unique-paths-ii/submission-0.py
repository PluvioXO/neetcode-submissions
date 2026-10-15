class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        seen = {} 
        def dfs(x: int, y: int):
            if x == len(obstacleGrid[0])-1 and y == len(obstacleGrid)-1 and obstacleGrid[y][x] == 0:
                return 1 
            if f"{x},{y}" in seen:
                return seen[f"{x},{y}"]
            if x == len(obstacleGrid[0]) or y == len(obstacleGrid):
                return 0 
            if obstacleGrid[y][x] == 1:
                return 0 
            mx = dfs(x+1, y)
            my = dfs(x,y+1)
            seen[f"{x},{y}"] = mx+my
            return mx+my
        return dfs(0,0)