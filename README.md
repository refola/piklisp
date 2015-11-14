# piklisp
NOTE: To avoid wasting time designing and implementing a poor copy of something that may already exist, I am suspending this project until after I find the time to learn [Arc](http://www.arclanguage.org), which I now realize likely improves at least as much on the "too many parentheses" state of Lisp as I could dream of doing on my own. [Here](http://stackoverflow.com/a/11579825/619001) is the Stack Overflow answer that brought me to this realization. I might eventually do a "piklisp.arc" (maybe "arc49"? I'm bad at naming projects) to implement [SRFI#49](http://srfi.schemers.org/srfi-49/srfi-49.html) in Arc. See also [piklisp.go](https://github.com/refola/piklisp.go) for an experimental Go-based Lisp that I'm making as a learning experience instead of trying to make the ultimate programming language.
-

Make Python-style programs via a Lisp dialect. Piklisp is a **P**ython**ic Lisp**. Piklisp is to have the appearance Python, combined with the power of everything you'd expect from a Lisp.

This is the design documentation. Implementation is not happening at this time.

# History
This is the successor to the stalled [Pyylisp](https://github.com/refola/pyylisp) project I was writing in Go. Instead of using Go to make a different way of displaying Lisp, I decided on using Python to make a Lisp interpreter that's integrated with Python. It's the simplest way I could think of to add "sufficiently powerful" metaprogramming to Python, while making it still look kinda like Python.

Piklisp used to be called Pyylisp.py, but "Pie-ee-lisp" kept feeling awkward to pronounce. Also, the correct term for "in a properly Python-like way" is "Pythonic", not "Pythony". Finally, I don't like the phonetic ambiguity of the English letter `c`, so I changed it to an unambiguous `k`.

Later on, I started realizing more and more of the complexities of designing a programming language. So I decided that this repo should focus on describing Piklisp instead of implementing it, dropping the language-specific `.py` from the end. Although there will still be examples of how the same concept would be expressed in Piklisp vs. other languages, there is no longer a canonical target implementation language.

# Future plans
Once the spec is mostly ironed out, I'll work on implementation. This is likely to be in a Lisp (e.g., [Scheme](http://schemers.org/) or [Clojure](http://clojure.org/)). However, since [C](https://en.wikipedia.org/wiki/C_%28programming_language%29) is the de-facto "glue code" language of the programming world, implementing Piklisp in C may maximize its usefulness.

# More info:
See the other .md files....

# Known bugs
None of this is implemented yet....

# See also
Although I came up with the idea of "Lisp with less parentheses" on my own, I am far from the first. Also, doing the [Common Lisp koans](https://github.com/google/lisp-koans) about halfway through a semester of Python made me see how Lisp macros would more elegantly solve problems I had in Python. So before working on the language spec, I did a lot of searches for how to replace Lisp parentheses with whitespace and also how to add Lisp macros to Python. Here are the most useful results I found from these searches. They all of which have implementations, but I haven't tested any of them.

* [SRFI 49 - Indentation-sensitive syntax](http://srfi.schemers.org/srfi-49/srfi-49.html) describes exactly what I wanted to do with Lisp. Other than shuffling around special characters a little to match Python instead of existing Lisps, Piklisp's syntax will match this. For the purpose of Piklisp, the only problem seems to be that SRFI 49 is written in Scheme (the "S" in SRFI) and not Python, but translating code should still be much easier than writing it all from scratch.
** [SRFI 110 - Sweet-expressions (t-expressions)](http://srfi.schemers.org/srfi-110/srfi-110.html) is a more syntax-heavy way of getting rid of even more parentheses and adding selective in-fix notation. This is of interest, but I feel it's too complicated for my ideal of a _simple_ Lisp that integrates with Python.
*** This branched off into the [Readable Lisp S-expressions Project](http://readable.sourceforge.net/), where it appears to be under active development.
** [wisp: Whitespace to Lisp](http://draketo.de/light/english/wisp-lisp-indentation-preprocessor) is a similar project made during the SRFI 110 discussion. It's much lighter on syntax than SRFI 110, but anything beyond the I-expressions of SRFI 49 feels like too much grouping syntax for me.
* [Logix](http://logix-language.sourceforge.net/index.html) ([GitHub link](https://github.com/tablatom/Logix)) is a programmable programming language built on Python2. It seems to have every language feature I could ask for, from indentation-based grouping, to Lisp-style semantic macros, to operator-specific infix notation. The project is unfortunately dorment.
* [MacroPy](https://github.com/lihaoyi/macropy) is a library for Python which adds macro support. It seems to work via imports and function decorators, making syntactic distinction between function calls and macros. To keep the language uncluttered, I can't use this for Piklisp. Also, based on how many times `print ` appears in the documentation relative to `print(`, I think it's only for Python2.
* [Metapython](https://code.google.com/p/metapython/) ([backup GitHub clone for when Google Code shuts down](https://github.com/refola/metapython)) is another project which adds macros to Python at import time. As with MacroPy, it seems to be for Python2. It also adds extra syntax.
