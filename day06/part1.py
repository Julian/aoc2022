import sys


for line in sys.stdin:
    print(
        next(
            i + 4
            for i in range(len(line) - 1)
            if len(set(line[i:i + 4])) == 4
        ),
    )
