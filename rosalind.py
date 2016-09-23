#!/usr/bin/python3
from itertools import permutations, groupby
from sys import argv


def find_overlap(left, right):
    min_overlap = min(len(left), len(right)) // 2 + 1
    overlap_start = left.find(right[:min_overlap])
    overlap = left[overlap_start:]
    if overlap_start != -1 and right.startswith(overlap):
        return len(overlap)


if __name__ == "__main__":
    filename = argv[1] if len(argv) > 1 else "rosalind_long.txt"
    # parse strands
    with open(filename) as f:
        stripped_lines = map(lambda l: l.strip(), f.readlines())
        dna_groups = (lines for is_label, lines
                      in groupby(stripped_lines, lambda l: l.startswith('>'))
                      if not is_label)
        strands = map("".join, dna_groups)
    # create adjacency list
    adj = {left: right
           for left, right in permutations(strands, 2)
           if find_overlap(left, right) is not None}
    # assemble
    right = super_strand = (adj.keys() - adj.values()).pop()
    while adj:
        left, right = right, adj.pop(right)
        super_strand += right[find_overlap(left, right):]

    print(super_strand)
