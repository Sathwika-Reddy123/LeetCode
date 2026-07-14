class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows=[set() for i in range(9)]
        cols=[set() for i in range(9)]
        boxes=[set() for i in range(9)]
        emp=[]
        for i in range(9):
            for j in range(9):
                if board[i][j]==".":
                    emp.append((i,j))
                else:
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    boxes[(i//3) * 3 + (j // 3)].add(board[i][j])
        
        def bt(k):
            if k == len(emp):
                return True

            i, j = emp[k]
            b = (i // 3) * 3 + (j // 3)
            for num in map(str, range(1, 10)):
                if num not in rows[i] and num not in cols[j] and num not in boxes[b]:
                    board[i][j] = num
                    rows[i].add(num)
                    cols[j].add(num)
                    boxes[b].add(num)

                    if bt(k + 1):
                        return True

                    board[i][j] = "."
                    rows[i].remove(num)
                    cols[j].remove(num)
                    boxes[b].remove(num)

            return False
        bt(0)

        