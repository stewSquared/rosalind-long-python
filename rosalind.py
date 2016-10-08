#!/usr/bin/python2
from sys import argv
from itertools import permutations, groupby


def find_overlap(left, right):  # (String, String) => Option[Int]
    min_overlap = min(len(left), len(right)) // 2 + 1
    overlap_start = left.find(right[:min_overlap])
    overlap = left[overlap_start:]
    if overlap_start != -1 and right.startswith(overlap):
        return len(overlap)


def adjacency_list(strands):  # Seq[String] => Map[String, String]
    adj = dict()
    rights_matched = set()  # For optimization. Don't use `adj.vaues()`
    for left, right in permutations(strands, 2):
        if left in adj or right in rights_matched:
            continue  # Short-circuit ~75% of iterations. Non-essential.
        if find_overlap(left, right):
            adj[left] = right
            rights_matched.add(right)
    return adj


def assemble(strands):  # Seq[String] => String
    adj = adjacency_list(strands)
    start_nodes = set(adj.keys()).difference(adj.values())
    assert(len(start_nodes) == 1)
    right = super_strand = start_nodes.pop()
    while adj:
        left, right = right, adj.pop(right)
        super_strand += right[find_overlap(left, right):]
    return super_strand


def fasta_strands(filename):  # String => Seq[String]
    with open(filename) as f:
        stripped_lines = (l.strip() for l in f.readlines())
        dna_groups = (lines for is_label, lines
                      in groupby(stripped_lines, lambda l: l.startswith('>'))
                      if not is_label)
        return map("".join, dna_groups)


if __name__ == "__main__":  # Option[String] => String
    filename = argv[1] if len(argv) > 1 else "rosalind_long.txt"
    print assemble(fasta_strands(filename))
