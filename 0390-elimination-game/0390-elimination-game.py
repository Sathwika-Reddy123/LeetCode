class Solution:
    def lastRemaining(self, n: int) -> int:
        def fun(n):
            if n==1:
                return 1
            return 2*((n//2)+1-fun(n//2))
        return fun(n)      
        