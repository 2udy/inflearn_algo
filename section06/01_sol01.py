'''
01 재귀함수를 이용한 이진수 출력

'''

def bin_num(N, result):
    if N != 0:
        result += str(N % 2)
        bin_num(N // 2, result)
    else:
        print(result[::-1])


N = int(input())
bin_num(N, '')
