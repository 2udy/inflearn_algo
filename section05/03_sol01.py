'''
03 후위표기식 만들기

'''

import sys
sys.stdin = open('03_input.txt')

in_order = input()
operators = []
ans = ''

for c in in_order:
    if c.isdecimal():
        ans += c
    elif c == '(':
        operators.append(c)
    elif c == ')':
        while operators:
            now_op = operators.pop()
            if now_op == '(':
                break
            ans += c
    elif c in ['+', '-']:
            while operators:
                now_op = operators.pop()
                if
                ans += operators.pop()
            operators.append(c)
    else:
        while operators:
            now_op = operators.pop()
            if now_op in ['*', '/']:
                ans += now_op
            elif now_op in ['+', '-']:
                operators.append(now_op)
                operators.append(c)
                break

    print(ans)



