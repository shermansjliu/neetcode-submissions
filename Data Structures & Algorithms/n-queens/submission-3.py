import copy
class Solution:
    def __init__(self):
        self.blocked_columns = set()
        self.blocked_positive_slope_diagonals = set()
        self.blocked_negative_slope_diagonals = set()
        self.queens_placed = 0
        self.res = []
        
    def can_place_queen(self, row, col, board):
        if row >= len(board) or col >= len(board):
            return False 

        if col in self.blocked_columns:
            return False

        if (row + col) in self.blocked_positive_slope_diagonals:
            return False

        if (row - col) in self.blocked_negative_slope_diagonals:
            return False

        return True
    def solveNQueens(self, n: int) -> List[List[str]]:
    
    ### search state (All columns on the next row )
    ### Invalid state
    ### Is valid queen state
    ### whether there's a queen on the positive diagonals or negative diagonals , row, or columns
        board = [["." for _ in range(n)] for _ in range(n)]
        self.dfs(0, board, n)
        return self.res
    def dfs(self, row, board, n):
        if self.queens_placed >= n:
            self.res.append(self.format(board))
            return
        
        for col in range(n):
            if not self.can_place_queen(row, col, board):
                continue
            pos_diag = row + col
            neg_diag = row - col
            board[row][col] = 'Q'
            self.blocked_columns.add(col)
            self.blocked_positive_slope_diagonals.add(pos_diag)
            self.blocked_negative_slope_diagonals.add(neg_diag)
            self.queens_placed += 1

            self.dfs(row + 1, board, n)

            self.queens_placed -= 1
            self.blocked_columns.remove(col)
            self.blocked_positive_slope_diagonals.remove(pos_diag)
            self.blocked_negative_slope_diagonals.remove(neg_diag)
            board[row][col] = '.'

    def format(self, board):
        formatted_board = []
        for row in board:
            formatted_board.append("".join(row))
        return formatted_board

    


