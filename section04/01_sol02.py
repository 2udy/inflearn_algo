import sys
sys.stdin = open('01_input.txt')


def bin_search(arr, key):
    start = 0
    end = len(arr) - 1
    while start <= end:
        middle = (start + end) // 2
        if arr[middle] < key:
            start = middle
        elif arr[(start + end) // 2] > key:
            end = middle
        else:
            return middle


N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
ans = bin_search(nums, M) + 1
print(ans)
