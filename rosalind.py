#!/usr/bin/python3
from itertools import permutations, groupby, starmap
from sys import argv


def find_overlap(left, right): # (String, String) => Option[Int]
    half_shorter = min(len(left), len(right)) // 2
    right_prefixes = (right[:i] for i in range(len(right), half_shorter, -1))
    return next(filter(left.endswith, right_prefixes), None)


def adjacency_list(strands): # Seq[String] => Map[String, (String, Int)]
    pairs = list(permutations(strands, 2))
    return {left: (right, len(overlap))
            for (left, right), overlap
            in zip(pairs, starmap(find_overlap, pairs))
            if overlap is not None}
    

def assemble(strands): # Seq[String] => String
    adj = adjacency_list(strands)
    start_nodes = adj.keys() - map(lambda tup: tup[0], adj.values())
    assert(len(start_nodes) == 1)
    node = super_strand = start_nodes.pop()
    while adj:
        node, overlap = adj.pop(node)
        super_strand += node[overlap:]
    return super_strand


def fasta_strands(filename): # String => Seq[String]
    with open(filename) as f:
        stripped_lines = map(lambda l: l.strip(), f.readlines())
        dna_groups = (lines for is_label, lines
                      in groupby(stripped_lines, lambda l: l.startswith('>'))
                      if not is_label)
        return map("".join, dna_groups)


if __name__ == "__main__": # Option[String] => String
    filename = argv[1] if len(argv) > 1 else "rosalind_long.txt"
    print(assemble(fasta_strands(filename)))
