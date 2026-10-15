"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        ans = 0
        rooms = 0
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])
        lp = 0 
        rp = 0 
        
        while lp < len(intervals):
            if start[lp] < end[rp]:
                rooms += 1
                ans = max(ans,rooms)
                lp += 1
            else:
                rooms -= 1
                rp += 1
        return ans 

        