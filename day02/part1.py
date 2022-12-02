import sys


SCORES = dict(X=1, Y=2, Z=3)
WINS = {"A Y\n", "B Z\n", "C X\n"}
DRAWS = {"A X\n", "B Y\n", "C Z\n"}


score = 0
for line in sys.stdin:
    _, _, selected = line.strip().partition(" ")
    score += SCORES[selected]

    if line in WINS:
        score += 6
    elif line in DRAWS:
        score += 3
print(score)
