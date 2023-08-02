'''
08 리스트와 내장함수
'''

b = list(range(1, 11))

print(b)
b.insert(3, -1)
b.insert(7, -1)
print(b)
b.remove(-1)
print(b)
print(b.index(-1))
print(sum(b))