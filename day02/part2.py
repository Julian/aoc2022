import sys


SCORES = dict(
    X=dict(A=3, B=1, C=2),
    Y=dict(A=4, B=5, C=6),
    Z=dict(A=8, B=9, C=7),
)


score = 0
for line in sys.stdin:
    them, _, result = line.strip().partition(" ")
    score += SCORES[result][them]
print(score)
