'''
07 송아지 찾기
'''
from collections import deque

MAX = 10000
dis = [0] * (MAX + 1)
visited = [0] * (MAX + 1)
S, E = map(int, input().split())

dQ = deque()
dQ.append(S)

dis[S] = 0

while dQ:
    now = dQ.popleft()
    if now == E:
        break
    for next in (now + 1, now - 1, now + 5):
        if 0 < next <= MAX:
            if visited[next]:
                pass
            else:
                dQ.append(next)
                visited[next] = 1
                dis[next] = dis[now] + 1
print(dis[E])


