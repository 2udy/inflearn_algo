'''
05 반복문을 이용한 문제풀이
1) 1부터 N까지 홀수 출력하기
2) 1부터 N까지의 합 구하기
3) N의 약수 출력하기
'''

N = int(input())
i = 0
# 1번
while i <= N:
    if i % 2 == 1:
        print(i, end=' ')
    i += 1
print()

# 2번
print(N*(N+1)//2)

# 3번
i = 1
while i <= N:
    if N % i == 0:
        print(i, end= ' ')
    i += 1


