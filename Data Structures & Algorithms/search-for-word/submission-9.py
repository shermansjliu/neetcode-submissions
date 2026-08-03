class Solution:
    def __init__(self):
        self.found = False

    def exist(self, board: List[List[str]], word: str) -> bool:
        word = list(word)
        visited = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(i, j, board, [], 0, word,visited )
                if self.found:
                    return True
        return False
    
    def dfs(self, i, j, board, state, char_pos, target_word_lst: List[str], visited):
        # lgtm
        if char_pos >= len(target_word_lst):
            if state == target_word_lst:
                print(state)
                self.found = True
            return

        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
            return 

        if (i,j) in visited:
            return

        if target_word_lst[char_pos] != board[i][j]:
            return

        for new_i, new_j in [(i,j+1), (i, j-1),(i+1,j),(i-1,j)]:
            visited.add((i,j))
            state.append(board[i][j])
            self.dfs(new_i, new_j, board, state, char_pos + 1, target_word_lst, visited)
            state.pop()
            visited.remove((i,j))

        