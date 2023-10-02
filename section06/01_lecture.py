'''
01 재귀함수를 이용한 이진수 출력

스택의 개념을 잘 이용할것
재귀 호출을 먼저 하고 프린트 하면 거꾸로 출력 가능
'''


def dfs(N):
    if N == 0:
        return
    else:
        dfs(N//2)
        print(N % 2, end='')


N = int(input())
dfs(N)
