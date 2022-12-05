from itertools import takewhile
import sys


picture = reversed(list(takewhile(lambda line: line != "\n", sys.stdin)))
stacks = [[] for _ in next(picture).split()]
for row in picture:
    for crate, stack in zip(row[1::4], stacks):
        if crate != " ":
            stack.append(crate)

for line in sys.stdin:
    count, _, rest = line[len("move "):].partition(" from ")
    origin_label, _, to_label = rest.partition(" to ")
    origin, to = stacks[int(origin_label) - 1], stacks[int(to_label) - 1]
    to.extend(origin[-int(count):])
    del origin[-int(count):]
print("".join(stack[-1] for stack in stacks))
