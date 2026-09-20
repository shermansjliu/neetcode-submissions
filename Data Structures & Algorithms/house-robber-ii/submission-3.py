class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums[0], nums[1])
        # rob first house, so can't rob last house
        temp_nums = nums[:len(nums)-1]
        dp = [0] * len(temp_nums)
        dp[0] = temp_nums[0]
        dp[1] = max(temp_nums[0], temp_nums[1])

        rob_first_house = 0
        for i in range(2, len(temp_nums)):
            _skip = dp[i-1]
            _rob = dp[i-2] + temp_nums[i]
            dp[i] = max(_skip, _rob)


        print(dp)
        rob_first_house = dp[-1]
        
        nums = nums[1:]
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        skip_first_house = 0
        for i in range(2, len(nums)):
            _skip = dp[i-1]
            _rob = dp[i-2] + nums[i]
            dp[i] = max(_skip, _rob)
        skip_first_house = dp[-1]

        res = max(skip_first_house, rob_first_house)
        return res