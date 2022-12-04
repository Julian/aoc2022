import sys


def to_range(elf_range):
    start_str, _, end_str = elf_range.partition("-")
    return int(start_str), int(end_str)


def overlap(first_elf, _, second_elf):
    first, second = sorted([to_range(first_elf), to_range(second_elf)])
    return first[0] == second[0] or first[1] >= second[1]


pairs = (line[:-1].partition(",") for line in sys.stdin)
print(sum(1 for pair in pairs if overlap(*pair)))
