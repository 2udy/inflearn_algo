'''
06 자릿수의 합

100/100

배열 새로 만들어서 max(배열)하지 말고
max값 변수로 주고 비교해서 최대값 구하는 방식으로 풀어보기

digit_sum함수 문자열 처리해서 구현 할 수도 있음
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
