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

I could return some sort of overlap object/tuple/datastructure that
stores the length of overlap, rather than just a string, so I don't
have to recompute overlap during assembly. I don't for two reasons:

 - find_overlap is only called O(N) times during assembly vs O(N^2)
   times during adjacency. Not likely to make 1% difference.

 - By not overdesigning for this special-case optimization, code is
   cleaner, more intuitive, and more re-useable.

I call `find_overlap` in `assemble` without first performing a None
check. This is safe, because of the pre-computed `adj`. But the
compiler doesn't know that. Renegade for life ;)

There are no tests; I used the REPL to develop. That said, code is
modular and testable, since this is TDD with tests thrown out.

Documentation is just comments with Scala type signatures. Sorry.


### Performance
(`time` 50, 500, and 5000 reads on a Xeon processor)
```
real    0m0.016s    0m0.232s    0m20.159s
user    0m0.010s    0m0.223s    0m20.140s
sys     0m0.003s    0m0.007s    0m0.017s
```
