class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def f(i,op,r,):
            if len(op)==k:
                r.append(op)
                return
            if i > n:
                return
            f(i+1,op+[i],r)  
            f(i+1,op,r)  
        r=[]
        f(1,[],r)
        return r