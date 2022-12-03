import sys


total = 0
for line in sys.stdin:
    second, third = next(sys.stdin), next(sys.stdin)
    badge, = set(line[:-1]).intersection(second[:-1]).intersection(third[:-1])
    if badge.isupper():
        total += ord(badge) - ord("A") + 27
    else:
        total += ord(badge) - ord("a") + 1
print(total)
