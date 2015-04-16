# pyylisp.py
Make Python-compatible programs via a Lisp dialect. Pyylisp is to have functions for everything you'd want to do in Python, combined with the power of everything you'd expect from a Lisp.

This is the successor to the stalled [Pyylisp](https://github.com/refola/pyylisp) project I was writing in Go. Instead of using Go to make a different way of displaying Lisp, I'm using Python to make a Lisp interpreter that's integrated with Python. It's the simplest way I could think of to add "sufficiently powerful" metaprogramming to Python, while making it still look kinda like Python.

# More info:
See the other .md files....

# Known bugs
None of this is implemented yet. I plan to have something useful ready by May, turning this into my final project for Python class.

# See also
Although I came up with the idea of "Lisp with less parentheses" on my own (much like most Lisp initiates), I am far from the first. Since I did the [Common Lisp koans](https://github.com/google/lisp-koans) about halfway through a semester of Python and saw how Lisp macros would more elegantly solve problems I had in Python, I also did a lot of searches for adding such macros to Python. Here are the most useful results I found from these searches. They all of which have implementations, but I haven't tested any of them.

* [SRFI 49 - Indentation-sensitive syntax](http://srfi.schemers.org/srfi-49/srfi-49.html) describes exactly what I wanted to do with Lisp. Other than shuffling around special characters a little to match Python instead of existing Lisps, Pyylisp's syntax will match this. For the purpose of Pyylisp, the only problem seems to be that SRFI 49 is written in Scheme (the "S" in SRFI) and not Python, but translating code should still be much easier than writing it all from scratch.
** [SRFI 110 - Sweet-expressions (t-expressions)](http://srfi.schemers.org/srfi-110/srfi-110.html) is a more syntax-heavy way of getting rid of even more parentheses and adding selective in-fix notation. This is of interest, but I feel it's too complicated for my ideal of a _simple_ Lisp that integrates with Python.
*** This branched off into the [Readable Lisp S-expressions Project](http://readable.sourceforge.net/), where it appears to be under active development.
** [wisp: Whitespace to Lisp](http://draketo.de/light/english/wisp-lisp-indentation-preprocessor) is a similar project made during the SRFI 110 discussion. It's much lighter on syntax than SRFI 110, but anything beyond the I-expressions of SRFI 49 feels like too much grouping syntax for me.
* [Logix](http://logix-language.sourceforge.net/index.html) ([GitHub link](https://github.com/tablatom/Logix)) is a programmable programming language built on Python2. It seems to have every language feature I could ask for, from indentation-based grouping, to Lisp-style semantic macros, to operator-specific infix notation. The project is unfortunately dorment.
* [MacroPy](https://github.com/lihaoyi/macropy) is a library for Python which adds macro support. It seems to work via imports and function decorators, making syntactic distinction between function calls and macros. To keep the language uncluttered, I can't use this for Pyylisp. Also, based on how many times `print ` appears in the documentation relative to `print(`, I think it's only for Python2.
* [Metapython](https://code.google.com/p/metapython/) ([backup GitHub clone for when Google Code shuts down](https://github.com/refola/metapython)) is another project which adds macros to Python at import time. As with MacroPy, it seems to be for Python2. It also adds extra syntax.


