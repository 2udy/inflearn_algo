'''
06 격자판 최대합

'''

import sys
import pprint
sys.stdin = open('06_input.txt')


def max_inline(arr, N):
    max_sum = 0
    for i in range(N):
        tmp = sum(arr[i])
        if tmp > max_sum:
            max_sum = tmp
    return max_sum


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
result = max_inline(board, N)
r_cross = 0
l_cross = 0

for i in range(N):
    for j in range(N):
        if i == j:
            l_cross += board[i][j]
        if i + j == N - 1:
            r_cross += board[i][j]

if l_cross > result:
    result = l_cross

if r_cross > result:
    result = r_cross

for i in range(N):
    for j in range(i + 1, N):
        board[i][j], board[j][i] = board[j][i], board[i][j]

if max_inline(board, N) > result:
    result = max_inline(board, N)

print(result)
