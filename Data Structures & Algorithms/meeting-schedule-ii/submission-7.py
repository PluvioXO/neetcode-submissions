"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        items = [(i.start, i.end) for i in intervals]
        events = []
        start, end = [], [] 
        for i in items:
            start.append(i[0])
            end.append(i[1])
        start.sort()
        end.sort()

        current, res = 0, 0 
        l,r = 0, 0 
        while l < len(start):
            if start[l] < end[r]:
                current += 1 
                l += 1
            else:
                current -= 1 
                r += 1
            res = max(res, current)
        return res; 
        
        
