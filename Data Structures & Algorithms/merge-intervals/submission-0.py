class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals

        intervals = sorted(intervals, key = lambda x: x[0])
        ans = [intervals[0]]

        for x in range(len(intervals)-1):
            if ans[-1][1] >= intervals[x+1][0] and ans[-1][1] <= intervals[x+1][1]:
                ans[-1][1] = intervals[x+1][1]
            elif ans[-1][1] < intervals[x+1][0]:
                ans.append(intervals[x+1])
        return ans