'''
03 부분집합 구하기(DFS)
'''

def partial(n):
    if n == N + 1:
        for i in range(1, n):
            if visited[i] == 1:
                print(i, end=' ')
        print()
    else:
        visited[n] = 1
        partial(n + 1)
        visited[n] = 0
        partial(n + 1)


N = int(input())
visited = [0] * (N + 1)

partial(1)

