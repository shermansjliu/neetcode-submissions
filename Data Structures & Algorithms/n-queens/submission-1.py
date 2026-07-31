class Solution:
    def __init__(self):
        self.res = [] 
    
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["." for _ in range(n)] for _ in range(n)]
        print(board)
        self.columns = set()
        self.down_diagonals = set()  # \
        self.up_diagonals = set()    # /
        
        self.dfs(0, 0, board)
        return self.res

    def can_place_queen(self, row, col, board):
        return (
            col not in self.columns
            and row - col not in self.down_diagonals
            and row + col not in self.up_diagonals
        )

    def convert(self, board):
         return ["".join(row) for row in board]

    def dfs(self, i, j, board):
        if i >= len(board):
            print("adding a board")
            self.res.append(self.convert(board))
            return 

        # place a queen and move into the next row
        for col in range(len(board)):
            if self.can_place_queen(i, col, board):
                # Place Q
                board[i][col] = 'Q'
                self.columns.add(col)
                # Explain how this works 
                self.down_diagonals.add(i - col)
                self.up_diagonals.add(i + col)    #)
                self.dfs(i + 1, col, board)

                # backtrack
                self.columns.remove(col)
                self.down_diagonals.remove(i - col)
                self.up_diagonals.remove(i + col)    #)
                board[i][col] = '.'