class Solution:
    def lastInteger(self, n: int) -> int:
        def fun(n):
            if n==1:
                return 1
            return 2*((n+1)//2+1 - fun((n+1)//2))-1
        return fun(n)