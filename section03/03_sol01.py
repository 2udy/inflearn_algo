'''
카드 역배치
'''

# import sys
# sys.stdin = open('03_input.txt')

cards = [i for i in range(21)]

for _ in range(10):
    a, b = map(int, input().split())
    for i in range((b - a + 1) // 2):
        print(i, cards[a + i], cards[b - i])
        cards[a + i], cards[b - i] = cards[b - i], cards[a + i]
for j in range(1, 21):
    print(cards[j], end=' ')