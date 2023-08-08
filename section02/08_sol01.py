'''
08 뒤집은 소수
'''


def reverse(ori_nums):
    rev_result = 0
    for ori_num in enumerate(ori_nums):
        rev_result += int(ori_num[1]) * (10**ori_num[0])
    return rev_result


def isPrime(y):
    if all(y % i != 0 for i in range(2, y - 1)):
        return True
    else:
        return False


N = int(input())
nums = list(input().split())
result = []

for num in nums:
    rev_num = reverse(num)
    if isPrime(rev_num):
        result.append(rev_num)

print(*result)
