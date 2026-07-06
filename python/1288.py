from typing import List

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key= lambda x: (x[0], -x[1]))
        remove = 0
        d = 0

        for _, b in intervals:
            if b > d:
                d = b
            elif b <= d:
                remove += 1
        
        return len(intervals) - remove