'''
05 수들의 합

'''

# import sys
# sys.stdin = open('05_input.txt')

N, M = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0

for i in range(N):
    for j in range(i, N):
        cnt = 0
        k = i
        while k <= j:
            cnt += arr[k]
            k += 1
        if cnt == M:
            ans += 1
print(ans)

