class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        set1 = set()

        for i in range(9):
            #Checks the row
            for x in board[i]:
                if x>= '1' and x <= '9':
                    if x in set1:
                        return False
                    else: 
                        set1.add(x)
            set1=set()
                
            #Checks the col 
            for i2 in range(9):
                if board[i2][i] >= "1" and board[i2][i] <= '9':
                    if board[i2][i] not in set1: 
                        set1.add(board[i2][i])
                    else:
                        return False
            set1 = set()

            for x in range(9):
                y1 = ((i//3)*3)+(x//3)
                x1 = ((i%3)*3)+(x%3)
                if board[y1][x1] >= '1' and board[y1][x1] <= '9':
                    if board[y1][x1] not in set1:
                        set1.add(board[y1][x1])
                    else:
                        return False 
            set1 = set()
        return True
            