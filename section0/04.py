'''
04 반복문(for, while, break, continue)
'''
a = range(10, 0)
print(type(a))

# continue

# for else 구문 : for 문이 break걸리지 않고 전체를 순회 하면 else문 실행
for i in range(10):
    print(i)
    if i > 5:
        break
else:
    print('for문 정상 순회')