class Solution:
    def longestPalindrome(self, s: str) -> str:
        """r=""
        def f(s):
            nonlocal r
            if len(s)==0:
                return 
            for i in range(len(s)):
                a=s[:i+1]
                if a==a[::-1] and len(a)>len(r):
                    r=a
            f(s[1:])
        f(s)
        return r   #brute force

        r=""
        def f(l,r):
            
            while l>=0 and r<len(s) and s[l]==s[r]:
                l-=1
                r+=1
            return s[l+1:r]
        for i in range(len(s)):
            x=f(i,i)
            y=f(i,i+1)
            r=max(r,x,y,key=length)
        return r """  #two pointers

        t=[[0]*len(s) for i in range(len(s))]
        for i in range(len(s)):
            t[i][i]=1
        start=0
        maxx=1
        for i in range(len(s)-1):
            j=i+1
            if s[i]==s[j]:
                t[i][j]=1
                start=i
                maxx=2
            
        for length in range(3,len(s)+1):
            for i in range(len(s)-length+1):
                j=i+length-1
                if s[i]==s[j] and t[i+1][j-1]==1:
                    t[i][j]=1
                    start=i
                    maxx=length
        return s[start:start+maxx]

        