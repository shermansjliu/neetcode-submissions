class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = float('-inf')
        
        dp_max = [float('-inf')] * len(nums)
        dp_min = [float('inf')] * len(nums)

        # dp i = longest contiguous product so far
        # How do you deal with negatives 
        # Keep max negatives? yes
        # dp_max = max(dp_max[i-1] * nums[i] if nums[i] positive else dp_min[i-1] * nums[i])
        # dp_min = inverse

        # res = max(dp_max[i])
        if len(nums) == 1:
            return nums[0]

        dp_max[0] = nums[0]
        dp_min[0] = nums[0]
        
        for i in range(1, len(nums)):
            dp_max[i] = max(dp_max[i-1] * nums[i], nums[i], nums[i] * dp_min[i-1])
            dp_min[i] = min(dp_min[i-1] * nums[i], nums[i], dp_max[i-1] * nums[i])
            res = max(dp_max[i], res)


            
        # print(dp_max)
        # print(dp_min)
        return res
        

        