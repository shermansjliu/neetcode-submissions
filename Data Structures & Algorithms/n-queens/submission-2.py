import copy
class Solution:
    def __init__(self):
        self.blocked_columns = set()
        self.blocked_positive_slope_diagonals = set()
        self.blocked_negative_slope_diagonals = set()
        self.queens_placed = 0
        self.res = []
        
    def solveNQueens(self, n: int) -> List[List[str]]:
    
    ### search state (All columns on the next row )
    ### Invalid state
    ### Is valid queen state
    ### whether there's a queen on the positive diagonals or negative diagonals , row, or columns

        board = [["." for _ in range(n)] for _ in range(n)]
        self.dfs(0, board, n)
        return self.res

    def format(self, board):
        formatted_board = []
        for row in board:
            formatted_board.append("".join(row))
        return formatted_board

    
    def dfs(self, i, board, n):
        if self.queens_placed >= n:
            self.res.append(self.format(board))
            return  


        '''
        (0,0) (-1, + 1) #/
        row -1, col + 1

        (0,0) (+1, + 1) # \
        '''

        
        ## add queen
        for j in range(n):
            if j in self.blocked_columns:
                continue

            if (i + j) in self.blocked_positive_slope_diagonals:
                continue

            if (i - j) in self.blocked_negative_slope_diagonals:
                continue

            board[i][j] = 'Q'
            self.blocked_positive_slope_diagonals.add(i + j)
            self.blocked_negative_slope_diagonals.add(i - j)
            self.blocked_columns.add(j)
            self.queens_placed += 1
    
            self.dfs(i + 1, board, n)
    
            self.queens_placed -= 1
            self.blocked_positive_slope_diagonals.remove(i + j)
            self.blocked_negative_slope_diagonals.remove(i - j)
            self.blocked_columns.remove(j)
            board[i][j] = '.'


