class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        dct = {0:1}
        res = 0
        prefix_sum = 0
        for i in range(len(nums)):
            prefix_sum += nums[i]
            looking_for = prefix_sum % k
            dct[looking_for] = dct.get(looking_for, 0)
            res += dct[looking_for]
            dct[looking_for] += 1
        return res
            
