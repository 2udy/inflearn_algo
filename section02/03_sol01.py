'''
03 K번째 큰 수
0/100 문제를 잘못 이해했구나 다시 풀도록 하자
'''
import sys
sys.stdin = open('03_input.txt')

N, K = map(int, input().split())
cards = list(map(int, input().split()))
cards.sort(reverse=True)

print(cards[K-1])
