'''
04 대표값

100/100

파이썬의 round함수는 round_half_even방식
round_half_up방식으로 소수 첫째 자리에서 반올림한 값을 구하려면....더보기
a = a + 0.5
int(a)
이렇게 해야 round_half_up 가넝!!!
'''
import sys
sys.stdin = open('04_input.txt')

N = int(input())
scores = list(map(int, input().split()))
represents = []
avg = int((sum(scores) / N) + 0.5)
diff = avg

for score in scores:
    if abs(avg - score) < diff:
        diff = abs(avg - score)
        represents = [score]
    elif abs(avg - score) == diff:
        represents.append(score)

print(avg, scores.index(max(represents)) + 1)
