class Solution:
    @cache
    def climbStairs(self, n: int) -> int:
        """if n==1:
            return 1
        if n==2:
            return 2
        dp=[1,2]
        for i in range(2,n):
            dp.append(dp[-1]+dp[-2])
        return dp[-1]  
        if n<=1:
            return 1
        return self.climbStairs(n-1)+self.climbStairs(n-2)   """   
        l=[-1]*(n+1)
        l[0]=1
        l[1]=1
        def f(n):
            if n<=1:
                return 1
            if l[n]!=-1:
                return l[n]
            l[n]=f(n-1)+f(n-2)
            return l[n]
        return f(n)
        