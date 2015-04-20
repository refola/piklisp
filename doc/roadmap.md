# Implementation stages
Building a language, even off the back of other languages, is a complex thing to do. To control the complexity, I'm implementing Piklisp in about 4 stages, outlined below.

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
* Finally, Piklisp can call itself a Lisp!
* This stage requires the Piklisp compiler to understand more than simple syntax translation rules.
** For example, it will have to keep track of namespaces, run functions, et cetera.
* This stage lays the groundwork for all the magic stuff in stage 2.

## Stage 2: Magic!
* This is where Piklisp goes from "Python-integrated Lisp with less parentheses" to "I come from Python Land and I want my parentheses back".
* With the magic of macros, all sorts of craziness can be done, without any more syntax than Python or Common Lisp.
* Example: Instead of the `=` macro just assigning values to variables, it can be made to cooperate with the `class` macro. Then `= my-object my-class arg` can set my-object equal to the value of `my-class arg` and, as if by **magic** also generate in-scope symbols for `my-object.method`, _without `.` even being in Piklisp's syntax_!
** I'm not _entirely_ sure if this expressivity is possible in Lisp. I need to practice more Lisp and see if I can make a macro that generates something that, when invoked by another macro, passes extra keyword arguments to the second macro to tell it what magic to make.
