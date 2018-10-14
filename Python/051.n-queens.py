#!/usr/bin/python3

"""
八皇后问题是一个以国际象棋为背景的问题：如何能够在8×8的国际象棋棋盘上放置八个皇后，使得任何一个皇后都无法直接吃掉其他的皇后？为了达到此目的，任两个皇后都不能处于同一条横行、纵行或斜线上。八皇后问题可以推广为更一般的n皇后摆放问题：这时棋盘的大小变为n×n，而皇后个数也变成n。当且仅当n = 1或n ≥ 4时问题有解[1]。

对于任意(x,y),如果要让新的点和它不能处于同一条横行、纵行或斜线上，则新点(p,q)必须要满足p+q != x+y 和p-q!= x-y, 前者针对左下右上斜线，后者针对左上右下斜线，两者同时都保证了不在同一条横行和纵行上。

代码中变量的含义:

cols_lst: 每一行皇后的column位置组成的列表
cur_row：目前正在判断的row的index
xy_diff：所有x-y组成的列表
xy_sum：所有x+y组成的列表
"""


class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def dfs(cols_lst, xy_diff, xy_sum):
            cur_row = len(cols_lst)
            if cur_row == n:
                ress.append(cols_lst)
            for col in range(n):
                if col not in cols_lst and cur_row - col not in xy_diff and cur_row + col not in xy_sum:
                    dfs(cols_lst + [col], xy_diff+[cur_row-col], xy_sum+[cur_row+col])

        ress = []
        dfs([], [], [])
        return [['.' * i + 'Q' + '.' * (n-i-1) for i in res] for res in ress]


sol = Solution()
output = sol.solveNQueens(5)
print(output)