import copy
class Solution:
    def __init__(self):
        self.res = []
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.dfs([], 0, target, candidates)
        return self.res

    def dfs(self, state, pos, t, candidates):

        if pos >= len(candidates):
            if t == 0:
                self.res.append(copy.copy(state))
                return 
            return
            
        if t < 0:
            return 
        
        state.append(candidates[pos])
        self.dfs(state, pos + 1, t - candidates[pos], candidates)
        state.pop()
        
        while pos + 1 < len(candidates) and candidates[pos] == candidates[pos+1]:
            pos += 1

        self.dfs(state, pos + 1, t, candidates)

        # self.dfs(state, pos + 1, t - candidates[pos], candidates)
        