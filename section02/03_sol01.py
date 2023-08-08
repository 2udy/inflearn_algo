'''
03 K번째 큰 수
'''
import sys
sys.stdin = open('03_input.txt')

N, K = map(int, input().split())
cards = list(map(int, input().split()))
cards.sort(reverse=True)

print(cards[K-1])
