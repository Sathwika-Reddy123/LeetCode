class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        a=[]
        for st,end in intervals:
            if not a or  st > a[-1][1]:
                a.append([st,end])
            else:
                a[-1][1]=max(end,a[-1][1])
        return a
        