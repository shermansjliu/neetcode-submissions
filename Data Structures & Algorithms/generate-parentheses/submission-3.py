class Solution:
    def __init__(self):
        self.res = []
    def generateParenthesis(self, n: int) -> List[str]:

        self.dfs([], 0, 0 , n)

        return self.res
    

    # let n be the number 
    def dfs(self, state, num_closed, num_open, n):
        if num_open > n or num_closed > n:
            return

        if len(state) == n*2:
            self.res.append("".join(state))
            return
        
        
        print(state)
        state.append("(")
        self.dfs(state, num_closed, num_open + 1, n)
        state.pop()
        if num_open > num_closed:
            state.append(")")
            self.dfs(state, num_closed + 1, num_open, n)
            state.pop()

