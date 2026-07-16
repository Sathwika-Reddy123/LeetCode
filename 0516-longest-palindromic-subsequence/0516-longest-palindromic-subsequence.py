class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        t=[[0]*len(s) for i in range(len(s))]
        for i in range(len(s)):
            t[i][i]=1
        for length in range(2,len(s)+1):
            for i in range(len(s)-length+1):
                j=length+i-1
                if s[i]==s[j]:
                    t[i][j]=2+t[i+1][j-1]
                else:
                    t[i][j]=max(t[i][j-1],t[i+1][j])
        return t[0][-1]
        