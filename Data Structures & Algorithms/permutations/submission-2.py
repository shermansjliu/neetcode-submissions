import copy
class Solution:
    def __init__(self):
        self.res = []
    def permute(self, nums: List[int]) -> List[List[int]]:

        self.dfs([], nums)
        return self.res

    def dfs(self, state, nums_left):
        # for each element generate a recusrive call with the ith element taken out

        if not nums_left:
            self.res.append(copy.deepcopy(state))
            return 
        
        for i in range(len(nums_left)):
            state.append(nums_left[i])
            self.dfs(state, nums_left[:i] + nums_left[i+1:])
            state.pop()


        



        