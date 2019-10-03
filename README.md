# Some experimentation with benchmarks.  

I saw an article that compared Python with some other languages, and claimed Python took 45 seconds to do something that (it seemed to me) should be much faster.

The article is here: https://modelingguru.nasa.gov/docs/DOC-2783

The benchmark I explored was the Look And Say Sequence, which is described here: https://en.wikipedia.org/wiki/Look-and-say_sequence

Essentially it's a sequence of numbers each of whose decimal representation is similar to how one would verbally describe the previous number.

    1223334444
    -> one 1, two 2's, three 3's, 4 four's
    -> 11223344
    -> two 1's, two 2's, two 3's, two 4's
    -> 21222324
    -> one 2, one 1, three 2's, one 3, one 2, one 4
    -> 121132131214
    etc.

The authors of the article used the sequence starting with `1223334444`, and computed the sequence of "order" 45, which I understand to mean a sequence that's 45 items long.  The latter numbers in that sequence have thousands or millions of digits, and the authors use the sequence to test a programming language's handling of "large strings".

My code for computing this sequence is in `lookandsay.py`.  It currently contains several versions, with some commented out.  A naive implementation did indeed run in about 45 seconds on my mid-2014 MacBook Pro (3GHz i7 with 16 GB ram; the authors use an i7 2.8 GHz Mac of some kind, but I don't know the year)  The fastest version of the code I was able to write, using Python's built in `io.StringIO` buffer class (but not the one using generator functions) ran in about 2.5 seconds, while the one with generators took about 5 seconds.  About 2 seconds of this is IO.  I was printing everything to the terminal, which I know is fairly slow.  I believe the authors were writing to a file.  I haven't tried that yet.

Further tools for optimization that I may explore at some point include profiling and Cython.  I don't see a reason why this shouldn't in principle  be able to approximately match Java's time of .05 seconds.  However the developer time needed to do such optimizations shouldn't be ignored; on the other hand, neither should the rarity or frequency of such performance needs for a given problem domain.  Oftentimes, Python is plenty fast and your bottleneck, if you have one, is IO.

Timing was done using the unix time command:

    $ time python3 lookandsay.py 1223334444 45

Initially I misinterpreted the Look And Say problem, and instead counted total occurrences, producing a string like "one 1, two two's" and so forth.  The code for that is in `seeandsay.py`, and the code to generate random strings of digits is in `randomstrings.py`.  These were invoked using:

    $ python3 randomstrings.py 45 100 | time python3 seeandsay.py

Runtime for this incorrect interpretation was .06 seconds.
