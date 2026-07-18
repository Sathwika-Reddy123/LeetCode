class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])
        shoot=points[0][1]
        c=1
        for st,end in points[1:]:
            if st> shoot:
                c+=1
                shoot=end
        return c