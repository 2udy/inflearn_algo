'''
04 대표값
'''
import sys
sys.stdin = open('04_input.txt')

N = int(input())
scores = list(map(int, input().split()))
represents = []
avg = round(sum(scores) / len(scores))
diff = avg

for score in scores:
    if abs(avg - score) < diff:
        diff = abs(avg - score)
        represents = [score]
    elif abs(avg - score) == diff:
        represents.append(score)

print(avg, scores.index(max(represents)) + 1)
