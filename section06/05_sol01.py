'''
바둑이 승차

'''

import sys
sys.stdin = open('05_input.txt')


def ride(i, weight, max_w, tsum):
    if weight + total - tsum < max_w :
        return

    if weight > C:
        print('무게 초과')
        return
    if i == N:
        if weight > max_w:
            max_w = weight
        return max_w
    else:
        ride(i + 1, weight + dogs[i], max_w, tsum + dogs[i])
        ride(i + 1, weight, max_w, tsum + dogs[i])


C, N = map(int, input().split())

dogs = [int(input()) for _ in range(N)]
total = sum(dogs)
max_weight = ride(0, 0, 0, 0)
print(max_weight)