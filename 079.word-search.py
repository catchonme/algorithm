#!/usr/bin/python3


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board:
            return False

        row = len(board)
        col = len(board[0]) if row else 0

        if row == 0:
            return False
        if row != 0 and col == 0:
            return False
        if not word or word == '':
            return True

        def dfs(i, j, idx):
            if i < 0 or j < 0 or i > row-1 or j > col-1 or board[i][j] != word[idx]:
                return False
            if idx == len(word) - 1:
                return True
            board[i][j] = '*'  # mark as visited
            res = dfs(i+1, j, idx+1) or dfs(i, j+1, idx+1) or dfs(i-1, j, idx+1) or dfs(i, j-1, idx+1)
            board[i][j] = word[idx]  # backtrack
            return res

        return any(dfs(i, j, 0) for i in range(row) for j in range(col))


boardInput = [
  ['A', 'B', 'C', 'E'],
  ['S', 'F', 'C', 'S'],
  ['A', 'D', 'E', 'E']
]
sol = Solution()
output = sol.exist(boardInput, 'ABCCE')
print(output)
