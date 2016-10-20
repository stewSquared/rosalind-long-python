## Usage

Mark executable or run with `python2 rosalind.py`. Takes a filename
(defaults to "rosalind_long.txt") and prints assembled strand.


## Caveats

`find_overlap` assumes (without loss of correctness) that left and
right are roughly the same length. Complexity is O(len(left)) rather
than O(min_overlap). Superstring relationships are not detected.

`adjacency_list` is not technically an adjacency list, whose type
would map `String -> List[String]` rather than `String -> String`.
This is fine for our case, where the path is linear and unique.

Computation of the adjacency_list is not guaranteed to find all
overlaps. It optimizes (read: uses magic numbers) for our case where
strands are roughly the same length and overlap by at least half.
Even so, computation of `match_sites` is still the bottleneck of the
algorithm by a long shot.

I call `find_overlap` in `assemble` without first performing a None
check. This is safe iff `adj` has no false positives.

There are no tests; I used the REPL to develop. That said, code is
modular and testable, since this is TDD with tests thrown out.

Documentation is just comments with Scala type signatures. Sorry.


### Performance
(Xeon processor, 50, 500, 5000, and 50000 reads)
```
real    0m0.020s    0m0.077s    0m0.796s    0m11.303s
user    0m0.007s    0m0.060s    0m0.730s    0m10.747s
sys     0m0.010s    0m0.013s    0m0.063s    0m0.553s
```
