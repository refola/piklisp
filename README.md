# pyylisp.py
Make Python-compatible programs via a Lisp dialect. Pyylisp is to have functions for everything you'd want to do in Python, combined with the power of everything you'd expect from a Lisp.

This is the successor to the stalled [Pyylisp](https://github.com/refola/pyylisp) project I was writing in Go. Instead of using Go to make a different way of displaying Lisp, I'm using Python to make a Lisp interpreter that's integrated with Python. It's the simplest way I could think of to add "sufficiently powerful" metaprogramming to Python, while making it still look mostly like Python.

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
If a Pyylisp list appears in a context where it is not an argument to something else, then it is treated as a function call. The first item in the list is the name of the function and everything else is an argument to the function.

## Object-oriented stuff
There is no object-oriented programming support, and likely never will be beyond what's required to minimally support fluent access to Python stuff. In the meantime, meditate on the difference between `function majorArg minorArg` and `majorArg.function minorArg`.

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

# Known Bugs
None of this is implemented yet. I plan to have something useful ready by May, turning this into my final project for Python class.

