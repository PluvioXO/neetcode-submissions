"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        newIntervals = [] 
        for i in intervals:
            newIntervals.append((i.start, i.end))

        l,r = [], [] 
        for i in newIntervals: 
            l.append(i[0])
            r.append(i[1])
        l.sort()
        r.sort()

        neededDays = 0 
        temp = 0
        idxL, idxR = 0, 0  
        while idxL < len(l):
            print(l[idxL], r[idxR], temp)
            if l[idxL] >= r[idxR]:
                temp -= 1 
                idxR += 1
            else:
                temp += 1
                idxL += 1 
                neededDays = max(neededDays, temp)
        return neededDays; 