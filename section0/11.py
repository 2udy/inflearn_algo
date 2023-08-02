'''
11. 함수 만들기
'''

def calcul(a, b):
    c = a + b
    d = a - b
    # 튜플의 형태로 여러 개의 값 리턴 가능
    return c, d

print(calcul(14,2))