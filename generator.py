#!/usr/bin/python3
import random
from itertools import *
from sys import argv


def gen_bases():
    while True:
        yield "CTAG"[random.getrandbits(2)]
    pass


def gen_strands(strand_length, overlap=0.67, bases=gen_bases()):
    offset = int(strand_length * (1 - overlap)) or 1
    while True:
        bases, copy = tee(bases)
        yield "".join(islice(bases, strand_length))
        bases = copy
        _ = next(islice(bases, offset - 1, offset))  # consume offset
    pass


def main(num_strands=50, strand_length=1000, label="Rosalind"):
    strands = list(islice(gen_strands(strand_length), num_strands))
    random.shuffle(strands)
    for i, strand in enumerate(strands):
        print(">" + label + "_" + str(i))
        for offset in range(0, len(strand), 60):
            print(strand[offset:offset+60])


if __name__ == "__main__":
    if len(argv) == 1:
        main()
    elif len(argv) == 2:
        main(num_strands = int(argv[1]))
    elif len(argv) == 3:
        main(num_strands = int(argv[1]), strand_length = int(argv[2]))
    else:
        print("Usage: generator.py [num_strands] [strand_length]")
