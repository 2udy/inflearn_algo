'''
06 자릿수의 합

'''


def digit_sum(origin_num):
    ans = 0
    while origin_num != 0:
        ans += origin_num % 10
        origin_num = origin_num // 10
    return ans


N = int(input())
nums = list(map(int, input().split()))
results = []

for num in nums:
    results.append(digit_sum(num))

print(nums[results.index(max(results))])
