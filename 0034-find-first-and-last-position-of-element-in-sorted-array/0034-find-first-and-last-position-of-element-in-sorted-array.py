class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        r=[]
        for i in range(len(nums)):
            if nums[i]!=target:
                i+=1
            elif nums[i]==target:
                r.append(i)
        if len(r)==0:
            return [-1,-1]
        return [r[0],r[-1]]
        