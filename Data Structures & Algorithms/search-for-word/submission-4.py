class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(x, y, s, seen) -> bool: 
            if s == "":
                return True
            if x < 0 or x >= len(board[0]) or y < 0 or y >= len(board):
                return False 
            i = s[0]
            s = s[1:]
            if board[y][x] == i and f"{x},{y}" not in seen:
                seen.add(f'{x},{y}')
                return dfs(x+1, y, s, seen.copy()) or dfs(x-1, y, s, seen.copy()) or dfs(x,y+1, s, seen.copy()) or dfs(x, y-1, s, seen.copy()) 
            return False
        for y in range(len(board)):
            for x in range(len(board[0])):
                if dfs(x,y, word, set()):
                    print(x,y)
                    return True
        return False