class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d={0:1}
        s=0
        c=0
        for i in nums:
            s+=i
            if s-k in d:
                c+=d[s-k]
            d[s]=d.get(s,0)+1
        return c