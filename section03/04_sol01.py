'''
04 두 리스트 합치기

100 / 100
'''

# import sys
# sys.stdin = open('04_input.txt')

N = int(input())
arr1 = list(map(int, input().split()))
M = int(input())
arr2 = list(map(int, input().split()))

ans = sorted(arr1 + arr2)

for i in range(len(ans)):
    print(ans[i], end=' ')
