'''
09 리스트와 내장함수 (2)
'''

a = [23, 34, 25, 67, 35]

for x in enumerate(a):
    print(x)
    print(type(x))

# all 함수: 모두 참인 경우에 만 True 반환
print(all(60 > x for x in a))
print(all(70 > x for x in a))

# any 함수: 한 번 이라도 참인 경우가 있다면 True 반환
print(any(20 > x for x in a))
print(any(60 > x for x in a))
