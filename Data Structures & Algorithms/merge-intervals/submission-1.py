class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda it: it[0])

        print(intervals)
        curr = intervals[0]
        res = [intervals[0]]
        for i in range(1,len(intervals)):
            if curr[1] >= intervals[i][0]:
                curr[1] = max(curr[1], intervals[i][1])
            else:
                curr = intervals[i]
                res.append(intervals[i])
                
        return res
        