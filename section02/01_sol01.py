'''
K 번째 약수
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
