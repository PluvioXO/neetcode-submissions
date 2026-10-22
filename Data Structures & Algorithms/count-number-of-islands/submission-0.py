class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        def search(y: int, x: int): 
            nonlocal seen
            if (y,x) in seen:
                return;
            seen.add((y, x))
            if y < -1 or y >= len(grid):
                return; 
            if x < -1 or x >= len(grid[0]):
                return; 
            if grid[y][x] != "1":
                return
            search(y-1, x)
            search(y+1, x)
            search(y, x+1)
            search(y, x-1)
        total = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == "1" and (y,x) not in seen:
                    total += 1 
                    ##print(seen)
                    search(y,x)
        return total; 