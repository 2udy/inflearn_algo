'''
09 주사위 게임

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
