'''
바둑이 승차

'''

import sys
sys.stdin = open('05_input.txt')


def ride(i, weight, max_w):
    if weight > C or i == N:
        print('무게 초과 혹은 인덱스초과')
        return
    else:
        if weight > max_w:
            max_w = weight
        ride(i + 1, weight + dogs[i], max_w)
        ride(i + 1, weight, max_w)
    pass


C, N = map(int, input().split())

dogs = [int(input()) for _ in range(N)]
max_weight = 0

ride(0, 0, max_weight)

print(dogs)

