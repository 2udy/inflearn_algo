'''
01 변수와 출력함수
'''

# 값교환
# a, b = 10, 20
# print(a, b)
# a, b = b, a
# print(a, b)
# 갑자기 궁금한거 그러면 값교환 세네개도 한번에 가능?
a, b, c, d = 1, 2, 3, 4
print(a, b, c, d)
a, b, c, d = c, d, a, b
print(a, b, c, d)

# 변수 타입
# float형은 8바이트 넘어가면 데이터 손실
f = 12.123456789123456789
print(f)
# 12.123456789123457

# 출력방식
# end는 프린트 마지막 처리 / 기본 값은 줄바꿈'/n'
print(a, b, c, d, end='')
# sep는 변수 사이 처리 / 기본값은  공백' '
print(a, b, c, d, sep='')


