'''
02 숫자만 추출

'''

chars = input()

# chars = 'g0rn2Td8dsofnT'
nums = []
ans = 0
divisor = 0

for char in chars:
    if char.isdigit():
        nums.append(int(char))

for i in range(len(nums)):
    ans += (10 ** (len(nums) - i - 1)) * nums[i]

for i in range(1, ans+1):
    if ans % i == 0:
        divisor += 1

print(ans)
print(divisor)

