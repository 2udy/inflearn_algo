'''
01 K 번째 약수
80/100
15번째 라인 K번째 약수가 N인 경우오류 발생
K번째 약수가 N보다 큰지 확인한 후에 i+1 해야한다.
'''

N, K = map(int, input().split())
i = 1
ans = 0

while K != 0:
    if N % i == 0:
        K -= 1
        ans = i
    i += 1

    if N % i == N:
        ans = -1
        break

print(ans)
