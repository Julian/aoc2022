import sys


count = maximum = 0
for line in sys.stdin:
    if line.strip():
        count += int(line)
    else:
        if count > maximum:
            maximum = count
        count = 0
        continue
print(maximum)
