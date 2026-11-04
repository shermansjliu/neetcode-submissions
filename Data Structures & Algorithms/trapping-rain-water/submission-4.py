class Solution:
    def trap(self, heights: List[int]) -> int:
        max_l_r = [0]*len(heights) 
        max_r_l = [0]*len(heights)


        max_l_r[0] = heights[0]
        for i in range(1, len(heights)):
            max_l_r[i] = max(max_l_r[i-1], heights[i])

        max_r_l[-1] = heights[-1]
        for i in range(len(heights)-2, -1, -1):
            max_r_l[i] = max(max_r_l[i+1], heights[i])
        
        water = 0

        for i in range(1,len(heights)-1):
            lowest_wall = min(max_l_r[i], max_r_l[i])
            water_amnt = max(lowest_wall - heights[i], 0)
            water += water_amnt

        return water