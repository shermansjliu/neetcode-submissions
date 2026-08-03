import copy
class Solution:
    def __init__(self):
        self.res = []
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.dfs([], nums, 0)
        return self.res

    def dfs(self, state, nums, i):
        if i >= len(nums):
            self.res.append(copy.copy(state))
            return
        used_at_this_level = set()
        used_at_this_level.add(nums[i])

        state.append(nums[i])
        i += 1
        self.dfs(state, nums, i)
        state.pop()
        # while i < len(nums) and nums[i] not in used_at_this_level:
        while i < len(nums) and nums[i] == nums[i - 1]:
            i += 1
        self.dfs(state, nums, i)
        # for i in range(start, len(nums)):
        #     nums_left.pop(i)
        #     state.append(nums[i])
        #     self.dfs(state, nums_left, i)
        #     state.pop()
            

            

        
        
        