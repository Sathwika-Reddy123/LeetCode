class Solution:
    def totalNQueens(self, n: int) -> int:
        rows,cols,negD,posD=set(),set(),set(),set()
        board=[['.']*n for i in range(n)]
        res=[]
        def bt(i):
            if i==n:
                res.append([''.join(p) for p in board])
                return
            for j in range(n):
                if i in rows or j in cols or  i+j in posD or i-j in negD or board[i][j]=='Q':
                    continue
                board[i][j]=="Q"
                rows.add(i),
                cols.add(j),
                posD.add(i+j),
                negD.add(i-j), 
                      
                bt(i+1)
                board[i][j]='.'
                rows.discard(i)
                cols.discard(j)
                posD.discard(i+j)
                negD.discard(i-j)
        bt(0)
        return len(res)
        