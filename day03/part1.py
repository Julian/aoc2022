import sys


total = 0
for line in sys.stdin:
    length = len(line) // 2
    first, second = line[:length], line[length:-1]
    for each in set(first).intersection(second):
        if each.isupper():
            total += ord(each) - ord("A") + 27
        else:
            total += ord(each) - ord("a") + 1
print(total)
