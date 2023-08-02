'''
07 문자열과 내장함수
'''

msg = "It is Time"
for c in msg:
    if c.isupper():
        print(c, end=' ')
print()

for c in msg:
    if c.islower():
        print(c, end=' ')
print()

for c in msg:
    if c.isalpha():
        print(c)
    print(ord(c))

print(chr(65))