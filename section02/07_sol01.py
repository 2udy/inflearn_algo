'''
07 소수(에라토스테네스 체)

any 조건문에서 range를 1부터 시작해서 답이 안나옴
( 1로는 무조건 나눠지니까 2부터 N-1까지 확인해야함)

20/100
case 2,3,4,5 Time Limit Exceeded
'''

N = int(input())
ans = 1
for candidate in range(3, N+1, 2):
    # all 함수 사용한 풀이
    if all(candidate % j != 0 for j in range(2, candidate)):
        ans += 1

    # any 함수 사용한 풀이
    # if any(candidate % j == 0 for j in range(2, candidate)):
    #     pass
    # else:
    #     ans += 1

print(ans)
