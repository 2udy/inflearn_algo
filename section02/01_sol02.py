'''
01 K 번째 약수
100/100

for else 구문으로도 풀어보기
'''

N, K = map(int, input().split())
i = 1
ans = 0

while K != 0:
    if N % i == 0:
        K -= 1
        ans = i

    if N % i == N:
        ans = -1
        break
    i += 1

print(ans)
