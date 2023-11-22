'''
04 합이 같은 부분집합

'''

import sys
sys.stdin = open('04_input.txt')


def partial(i):
    if i == N:
        cnt = 0
        print(visited)
        for j in range(N):
            if visited[j] == 1:
                cnt += arr[j]
        return cnt
    else:
        visited[i] = 1
        partial(i + 1)
        visited[i] = 0
        partial(i + 1)


N = int(input())
arr = list(map(int, input().split()))
visited = [0] * N
total = sum(arr)
if total == total - partial(0):
    print('YES')
else:
    print('No')
