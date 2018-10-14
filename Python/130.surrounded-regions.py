#!/usr/bin/python3

import collections
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead
        """
        def legal(x, y):
            return x >= 0 and x < row and y >= 0 and y < col and board[x][y] == '0' and visited[x][y] == 0

        row = len(board)
        col = len(board[0]) if row else 0

        visited = [[0 for i in range(col)] for j in range(row)]

        notChange0Area = []
        queue = collections.deque()

        for j in range(col):
            if board[0][j] == '0': queue.append((0, j))
            if board[row-1][j] == '0': queue.append((row-1, j))
        for i in range(row):
            if board[i][0] == '0': queue.append((i, 0))
            if board[i][col-1] == '0': queue.append((i, col-1))

        while queue:
            (x, y) = queue.popleft()
            board[x][y] = '$'
            visited[x][y] = 1
            if legal(x-1, y):
                queue.append((x-1, y))
            if legal(x+1, y):
                queue.append((x+1, y))
            if legal(x, y-1):
                queue.append((x, y-1))
            if legal(x, y+1):
                queue.append((x, y+1))

        for i in range(row):
            for j in range(col):
                if board[i][j] == '$':
                    board[i][j] = '0'
                elif board[i][j] == '0':
                    board[i][j] = 'X'