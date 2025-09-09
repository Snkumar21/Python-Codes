class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        rows, cols = len(board), len(board[0])
        word_len = len(word)

        def dfs(r, c, idx):
            # if we matched all chars in word
            if idx == word_len:
                return True
            # out of bounds or not matching
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[idx]:
                return False

            # temporarily mark visited
            temp, board[r][c] = board[r][c], "#"

            # explore neighbors (up, down, left, right)
            found = (dfs(r+1, c, idx+1) or
                    dfs(r-1, c, idx+1) or
                    dfs(r, c+1, idx+1) or
                    dfs(r, c-1, idx+1))

            # restore original value (backtrack)
            board[r][c] = temp
            return found

        # try starting from every cell
        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True
        return False