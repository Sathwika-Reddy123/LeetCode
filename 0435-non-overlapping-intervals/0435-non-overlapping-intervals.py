class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        c=0
        prev_end=intervals[0][1]
        for st,end in intervals[1:]:
            if st>= prev_end:
                prev_end=end
            else:
                c+=1
        return c
        