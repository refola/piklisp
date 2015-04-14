# pyylisp.py
Make Python-compatible programs via a Lisp dialect. Pyylisp is to have functions for everything you'd want to do in Python, combined with the power of everything you'd expect from a Lisp.

This is the successor to the stalled [Pyylisp](https://github.com/refola/pyylisp) project I was writing in Go. Instead of using Go to make a different way of displaying Lisp, I'm using Python to make a Lisp interpreter that's integrated with Python. It's the simplest way I could think of to add "sufficiently powerful" metaprogramming to Python, while making it still look kinda like Python.

# Language Spec
Pyylisp tries to match Python as much as possible, so the spec is defined in terms of what's different. Everything that doesn't work like in Python and isn't specified in the spec is a bug.

## Things and thing separators
In Pyylisp, the only types of things are functions, lists, and Python values. Function names and Python values are written like in Python. However, lists are grouped differently than in Python, as explained below. For now, know that the only separators for things are the whitespace characters (space, tab, and newline); commas are not used.

## Lists, arrays, tuples, and iterators
Pyylisp treats everything as a list. So you can do things like using slice expressions on an iterator. The nth item of a list can be gotten via `[] mylist i` and a slice may be gotten via `[:] mylist m n`, which act like Python's `mylist[i]` and `mylist[m:n]`, respectively.

## Grouping things
To group things into lists, Pyylisp uses a combination of Python-style indentation-based grouping and Lisp-style parentheses-based grouping.

### Indentation-based grouping
A line followed by more-indented lines starts a group. Returning to a not-greater indentation level ends a group.

If a line is not followed by a more-indented line but it contains multiple things, then it acts as a group.

### Parentheses-based grouping
You can still use parentheses for grouping; this is recommended for things that look better on one line and this is necessary for making singleton lists.

## Functions
Because doing things is the most common thing to do in a program, the default interpretation of a list is a function followed by its arguments. To use a list as data instead, precede it with a single quote like `'(this is a quoted list)`. Macros should be able to do fancy stuff to change this or something.

## Object-oriented stuff
I think that something like `. object field subfield` is the "right" way to retrieve what would be referred to as `object.field.subfield` and `. object method argument` is the way to do `object.method(argument)`. An object is just a templated dictionary with syntactic sugar, so it's not a big deal anyway.

## Python keywords and syntax
Everything you can do with Python keywords and syntax is available in Pyylisp. However, all that stuff has been turned into functions. For example, instead of

	for x in y:
		print(x)

you can say

	for-in x y
		print x

## Lisp macros
I know that "macros" are meant to be like the holy grail of programming expressiveness power that turns every Lisp practitioner into a sanctified zealot or some such. However, I can't build them until I learn them. I'll probably write the Pyylisp macro system as soon as it seems like the most urgent/immediately-useful thing.

Note that half the Python I know is from searching for ways to avoid repeating myself in code. I expect that this is the force that will lead me to eventual understanding of Lisp macros.

# Known bugs
None of this is implemented yet. I plan to have something useful ready by May, turning this into my final project for Python class.

# Implementation stages
Building a language, even off the back of other languages, is a complex thing to do. To control the complexity, I'm implementing Pyylisp in about 4 stages, outlined below.

## Stage 0a: It does stuff!
* A Lisp-like syntax can be used to generate Python code, but it has all those annoying parentheses _and_ doesn't even provide the Lisp macros that make it worth wading through parentheses in the first place.
* This is the minimal prototype level of implementation, but it's kinda useless, so call it version zero.

## Stage 0b: Re-unparenthesize!
* Based on indentation levels, enough parentheses are removed that they stop being annoying.
** You're still stuck with required parentheses being ordered differently than in Python, but even most of those will be going away later....
* This is the same as [Scheme Request For Implementation 49](http://srfi.schemers.org/srfi-49/srfi-49.html).
* This is likely to be implemented before macros, because it's simpler, and there's already freely-licensed code that I think I can just translate from Scheme to Python.
* Stage 0b is so-called because its syntactic changes are orthogonal to the semantic augmentations and changes of stages 1 and 2. Technically, there could be a stage 1a or even 2a, but 0b is likely to prevent that.

## Stage 1: Macros!
* Finally, Pyylisp can call itself a Lisp!
* This stage requires the Pyylisp compiler to understand more than simple syntax translation rules.
** For example, it will have to keep track of namespaces, run functions, et cetera.
* This stage lays the groundwork for all the magic stuff in stage 2.

## Stage 2: Magic!
* This is where Pyylisp goes from "Python-integrated Lisp with less parentheses" to "I come from Python Land and I want my parentheses back".
* With the magic of macros, all sorts of craziness can be done, without any more syntax than Python or Common Lisp.
* Example: Instead of the `=` macro just assigning values to variables, it can be made to cooperate with the `class` macro. Then `= my-object my-class arg` can set my-object equal to the value of `my-class arg` and, as if by **magic** also generate in-scope symbols for `my-object.method`, _without `.` even being in Pyylisp's syntax_!
** I'm not _entirely_ sure if this expressivity is possible in Lisp. I need to practice more Lisp and see if I can make a macro that generates something that, when invoked by another macro, passes extra keyword arguments to the second macro to tell it what magic to make.

# See also
Although I came up with the idea of "Lisp with less parentheses" on my own (much like most Lisp initiates), I am far from the first. Since I did the [Common Lisp koans](https://github.com/google/lisp-koans) about halfway through a semester of Python and saw how Lisp macros would more elegantly solve problems I had in Python, I also did a lot of searches for adding such macros to Python. Here are the most useful results I found from these searches. They all of which have implementations, but I haven't tested any of them.

* [SRFI 49 - Indentation-sensitive syntax](http://srfi.schemers.org/srfi-49/srfi-49.html) describes exactly what I wanted to do with Lisp. Other than shuffling around special characters a little to match Python instead of existing Lisps, Pyylisp's syntax will match this. For the purpose of Pyylisp, the only problem seems to be that SRFI 49 is written in Scheme (the "S" in SRFI) and not Python, but translating code should still be much easier than writing it all from scratch.
** [SRFI 110 - Sweet-expressions (t-expressions)](http://srfi.schemers.org/srfi-110/srfi-110.html) is a more syntax-heavy way of getting rid of even more parentheses and adding selective in-fix notation. This is of interest, but I feel it's too complicated for my ideal of a _simple_ Lisp that integrates with Python.
*** This branched off into the [Readable Lisp S-expressions Project](http://readable.sourceforge.net/), where it appears to be under active development.
** [wisp: Whitespace to Lisp](http://draketo.de/light/english/wisp-lisp-indentation-preprocessor) is a similar project made during the SRFI 110 discussion. It's much lighter on syntax than SRFI 110, but anything beyond the I-expressions of SRFI 49 feels like too much grouping syntax for me.
* [Logix](http://logix-language.sourceforge.net/index.html) ([GitHub link](https://github.com/tablatom/Logix)) is a programmable programming language built on Python2. It seems to have every language feature I could ask for, from indentation-based grouping, to Lisp-style semantic macros, to operator-specific infix notation. The project is unfortunately dorment.
* [MacroPy](https://github.com/lihaoyi/macropy) is a library for Python which adds macro support. It seems to work via imports and function decorators, making syntactic distinction between function calls and macros. To keep the language uncluttered, I can't use this for Pyylisp. Also, based on how many times `print ` appears in the documentation relative to `print(`, I think it's only for Python2.
* [Metapython](https://code.google.com/p/metapython/) ([backup GitHub clone for when Google Code shuts down](https://github.com/refola/metapython)) is another project which adds macros to Python at import time. As with MacroPy, it seems to be for Python2. It also adds extra syntax.


