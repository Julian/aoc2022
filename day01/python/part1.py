import itertools
import sys


groups = itertools.groupby(sys.stdin, lambda line: bool(line.strip()))
most_calories = max(
    sum(int(line) for line in lines)
    for is_elf, lines in groups
    if is_elf
)
print(most_calories)
