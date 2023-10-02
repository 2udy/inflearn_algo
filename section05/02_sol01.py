'''
쇠 막대기

'''

import sys
sys.stdin = open('02_input.txt')

gwalhos = input()
cnt = 0
stick = []

for i in range(len(gwalhos)):
    if gwalhos[i] == '(':
        stick.append(gwalhos[i])
    elif gwalhos[i] == ')' and gwalhos[i-1] == ')':
        cnt += 1
        stick.pop()
    else:
        stick.pop()
        cnt += len(stick)

print(cnt)
