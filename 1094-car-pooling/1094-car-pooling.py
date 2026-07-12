class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        d=[0]*1001
        for i in trips:
            d[i[1]]+=i[0]
            d[i[2]]-=i[0]
        current=0
        for i in d:
            current+=i
            if current > capacity:
                return False
        return True        