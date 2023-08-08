'''
02 K번째 수
100/100
'''

import sys
sys.stdin = open('02_input.txt')

T = int(input())

for tc in range(T):
    N, s, e, k = map(int, input().split())
    nums = list(map(int, input().split()))[s-1:e]
    print(f'#{tc + 1} {sorted(nums)[k-1]}')
