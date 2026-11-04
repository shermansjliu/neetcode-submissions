from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)

        count[0] = 1
        prefix_sum = 0 
        res = 0
        # r - l = k 
        # l = r - k
        for i in range(len(nums)):
            prefix_sum += nums[i]
            looking_for = prefix_sum - k
            res += count[looking_for]
            count[prefix_sum] += 1
        return res

        