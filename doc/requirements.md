# Requirements for Piklisp
This is what Piklisp should do and have ways of doing.



# Metarequirements
This lists the general goals of Piklisp, the things that the requirements should support. These are mostly pretty general, so they are elaborated upon in the other sections.

1. It must be a Lisp. I.e., it must have syntactic macro support and be homoiconic. This is essential for the elimination and modularization of the "boilerplate" code seen in other languages.
2. It should be as simple and easy to use as the task it's used for. The language should be usable and general purpose.
3. It should look more like Python than Lisp. This is because all those parentheses are annoying enough to keep most people from using Lisps, while Python looks clean and tidy.



# Functional requirements
These are the functional requirements, sorted roughly from simplest to most complex.


## Using functions
* Must have input/output functions.
* Must support basic math functions.
* Must support bitwise operators.


## Making functions
* Must have a way of making functions
* User functions must be able to accept arguments of these types:
** Positional
** Optional
** Keyword
** Variadic
** Combinations of the above (TODO: figure out which combinations)
* Functions must be creatable independent of naming them (i.e., full lambda support)
* Functions must be creatable within global, function, module, and class scopes.
* Functions must be treated like other variables, i.e., able to be return values, items in lists, et cetera


## Variable-handling
* 


## Types
* 


## Classes
* 


## Modules
* 



# Aesthetic requirements
* Minimize use of parentheses (see SRFI 49 for indentation-based grouping, then consider how builtin functions and macros can eliminate even more parentheses)
* Minimize number of syntactic elements required to solve a problem
