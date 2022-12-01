import heapq
import itertools
import sys


groups = itertools.groupby(sys.stdin, lambda line: bool(line.strip()))
calories = (
    sum(int(line) for line in lines)
    for is_elf, lines in groups
    if is_elf
)
three_largest = heapq.nlargest(3, calories)
print(sum(three_largest))
