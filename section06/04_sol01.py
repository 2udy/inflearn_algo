'''
04 합이 같은 부분집합


sys.exit(0) 는 전체 프로그램 종료
partial 함수에서 프로그램이 종료 안되면 NO가 출력 됨

문제 이해 차근차근 제대로 하기
'''

import sys
sys.stdin = open('04_input.txt')


def partial(i, cnt):
    # pruning
    if cnt > total // 2:
        return
    if i == N:
        if total - cnt == cnt:
            print('YES')
            sys.exit(0)
    else:
        partial(i + 1, cnt + arr[i])
        partial(i + 1, cnt)


N = int(input())
arr = list(map(int, input().split()))
visited = [0] * N
total = sum(arr)

if total % 2 == 1:
    print('NO')
else:
    partial(0, 0)
    print('NO')
