'''
01 회문 문자열 검사

100 / 100
'''

# import sys
# sys.stdin = open('01_input.txt')
N = int(input())

for tc in range(N):
    word = input().lower()

    for i in range(len(word)):
        if word[i] == word[-i-1]:
            pass
        else:
            print(f'#{tc+1} NO')
            break
    else:
        print(f'#{tc+1} YES')
