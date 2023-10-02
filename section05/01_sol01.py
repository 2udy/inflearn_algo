'''
01 가장 큰 수

'''
import sys
sys.stdin = open('01_input.txt')

num, cnt = input().split()
cnt = int(cnt)
res = [num[0]]

for i in range(1, len(num)):
    for j in range(len(res)):
        if res[-1] < num[i] and cnt != 0:
            res.pop()
            cnt -= 1
    res.append(num[i])

for _ in range(cnt):
    res.pop()

for r in res:
    print(r, end='')





