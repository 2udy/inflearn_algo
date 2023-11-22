'''
08 사과나무(BFS)
'''

from collections import deque
import sys
sys.stdin = open('08_input.txt')
N = int(input())
apples = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
L = 0
Q = deque()

Q.append((N//2, N//2))
total = apples[N//2][N//2]
visited[N//2][N//2] = 1

while Q:
    if L == N // 2:
        break
    k = len(Q)
    for i in range(k):
        tmp = Q.popleft()
        for j in range(4):
            x = tmp[0] + dx[j]
            y = tmp[1] + dy[j]
            if visited[x][y]:
                pass
            else:
                total += apples[x][y]
                visited[x][y] = 1
                Q.append((x, y))
    L += 1
    
print(total)
