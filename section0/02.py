'''
02 변수 입력과 연산자
'''
# 연산자
a, b = map(int, input('숫자를 두 개 입력하세요 : ').split())
print('a + b = ', a + b)
print('a - b = ', a - b)
print('a * b = ', a * b)
print('a / b = ', a / b)
print('a // b = ', a // b)
print('a % b = ', a % b)
print('a ** b = ', a ** b)

# split
c = input("숫자를 여러개 입력하세요 :").split()
print(type(c))
print(c)
