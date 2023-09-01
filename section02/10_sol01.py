'''
10 점수계산

100/100

앞에 값이랑 비교할 필요 없이 그냥 현재 값으로 가중치만 줘도 풀이 가능
'''
import sys
sys.stdin = open('10_input.txt')

N = int(input())
results = list(map(int, input().split()))
score = 0
crnt_point = 0

if results[0] == 1:
    score += 1
    crnt_point = 1

for i in range(1, N):
    if results[i-1]:
        if results[i]:
            crnt_point += 1
        else:
            crnt_point = 0
    else:
        if results[i]:
            crnt_point = 1
        else:
            crnt_point = 0

    score += crnt_point

print(score)
