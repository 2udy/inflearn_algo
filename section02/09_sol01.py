'''
09 주사위 게임

100/100

games배열 없이 그냥 반복문 돌면서 인풋 바로 조건문 돌리고
rewards 배열대신 변수로 값 지정해서 비교해서 최대값 찾는 방식으로도 풀이 가능
'''

import sys
sys.stdin = open('09_input.txt')

N = int(input())
games = []
rewards = []

for _ in range(N):
    games.append(list(map(int, input().split())))

for game in games:
    cnt = [0, 0, 0, 0, 0, 0, 0]

    for num in game:
        cnt[num] += 1

    if max(cnt) == 3:
        rewards.append(10000 + cnt.index(3) * 1000)
    elif max(cnt) == 2:
        rewards.append(1000 + cnt.index(2) * 100)
    elif max(cnt) == 1:
        rewards.append(max(game) * 100)

print(max(rewards))
