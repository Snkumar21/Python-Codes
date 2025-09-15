class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res = []
        board = [["."] * n for _ in range(n)]

        # Sets to track attacks
        cols = set()
        posDiag = set()   # r + c
        negDiag = set()   # r - c

        def backtrack(r):
            if r == n:  # All rows filled -> valid solution
                res.append(["".join(row) for row in board])
                return
            
            for c in range(n):
                if c in cols or (r + c) in posDiag or (r - c) in negDiag:
                    continue  # Attack conflict, skip
                
                # Place queen
                board[r][c] = "Q"
                cols.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)

                # Recurse to next row
                backtrack(r + 1)

                # Undo move (backtrack)
                board[r][c] = "."
                cols.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)

        backtrack(0)
        return res