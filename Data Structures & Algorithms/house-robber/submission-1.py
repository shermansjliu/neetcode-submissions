class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = [0] * len(nums) 
        dp[0] = nums[0]

        for i in range(1,len(nums)):
            rob_this_house = dp[i-2] + nums[i]
            skip_this_house = dp[i-1]

            dp[i] = max(rob_this_house, skip_this_house)
        return dp[-1]

            
            