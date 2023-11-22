import sys
sys.stdin = open('01_input.txt')

N, M = map(int, input().split())

nums =sorted(list(map(int, input().split())))

print(nums.index(M) + 1)