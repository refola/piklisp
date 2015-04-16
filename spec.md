# About this spec
This is what Pyylisp aims to be. As of 2015-02-15, there is no implementation. Details are almost certain to change during the process of implementation. See roadmap.md for broad implementation stage plans. As soon as something minimally resembling the goal is achieved, version 0 will be announced and a changelog will be started. For now, it's just a bunch of ideas for a better language.



# Pyylisp language spec - rationale and goals
Pyylisp tries to match Python style as much as possible while keeping things simple and enabling Lisp macros. Here's an overview of what Pyylisp attempts to inherit from Python and Lisp.


## Pythonic goals
Pyylisp tries to avoid parentheses as much as possible without sacrificing clarity. So it should look like a funky dialect of Python, despite being a Lisp. Pyylisp also aims to be interoperable with Python, ranging from mimicing Pythonic style to compiling to Python.
* Pyylisp can access Python functions and classes as if they are in Pyylisp (same-named functions notwithstanding).
** E.g., `myfunc arg1 arg2` will call the Pyylisp `myfunc` if it exists. Otherwise it calls Python's `myfunc(arg1 arg2)`.
* Pyylisp functions and classes are accessible from Python is if they were written in it.
* Pyylisp uses Python's data types (int, float, string, list, tuple, dict, set, et cetera).
* Pyylisp has builtin functions for everything Python has syntax or keywords for.
** E.g., Pyylisp does `[] mylist index` to match Python's `mylist[index]`.
** E.g., Pyylisp does `for-in x (range 10)` to match Python's `for x in range(10)`.
* Pyylisp uses Python-style indentation-based grouping (so no Labyrinthianly Infuriating Superfluous Parentheses, or whatever your preferred backronym for Lisp happens to be).
* Pyylisp enables manual access to Python stuff via calls to `--py--`.
* Anything Pythonic that Pyylisp doesn't replace, you can easily do the Python version of in Pyylisp.


## Lispiness goals
While being Python-integrated and compatible, Pyylisp, despite its much-reduced use of parentheses, is also a Lisp. This results in a few limitations, but in return provides the ability to program the language itself.
* When parentheses are necessary for grouping, function calls look like `(myfunc arg1 arg2)` instead of the `myfunc(arg1, arg2)` traditional in C-family languages.
* Math looks funny because it's in prefix notation. There's room for a `math` function to enable things like `math 5 + 4 * 3 ** 2` instead of `+ 5 (* 4 (** 3 2))`, but language regularity prevents infix notation from being auto-accessible everywhere.
* Functions are just lists, so you can manipulate them like lists. This is where things start getting too powerful for easy Python integration....
* Macros can be simply defined to extend the language in ways that functions cannot. This is proper Lisp macros, not mere eval().
** For example,
	= show-and-print macro * code
		` print (fmt "%s evaluates to %s" ',@code ,@code)
** can be ran as `show-and-print foo` to yield, e.g., "foo evaluates to 42", regardless of how the caller's scope relates to show-and-print's scope. The Python version,
	def showAndPrint(code):
		print("%s evaluates to %s" % (code, eval(code)))
** looks like it would do the same as the Pyylisp when called with `showAndPrint("foo")`. If you just enter the function and call in Python's console, it will indeed print out "foo evaluates to 42" or whatever. _However_, try calling the Python "showAndPrint" from within a function it suddenly it can't find your variables. Pyylisp macros can find your variables.



# Syntax
Although Pyylisp strives to minimize syntax, it still has some. Here's the syntax so far.


## Grouping things
Like other Lisps and Python, Pyylisp allows you to group things into lists via parentheses. The difference from Python is that list items are separated by spaces, not commas. Here's an example list.
	(1 "two" three)
Like Python and unlike most Lisps, Pyylisp also uses indentation for grouping. This is like Scheme's [SRFI 49](http://srfi.schemers.org/srfi-49/srfi-49.html). Here's a factorial function without any parentheses.
	= factorial fn n
		if
			< n 2
			1
			* n
				this
					- n 1
Here's how parentheses are inferred from the indentation. Note that it is an error to write out indentation-inferred parentheses, since that's essentially doubling them.
	(= factorial fn n
		(if
			(< n 2)
			1
			(* n
				(this
					(- n 1)))))
Here's how the function would normally be written, combining indentation and parentheses to make it maximally readable.
	= factorial fn n
		if (< n 2)
			1
			* n (this (- n 1))
Note for Lispers: The `=` macro "cheats" to get rid of the parentheses that would normally surround the `fn` macro call. `=` evaluates everything after its first argument and sets the symbol of the first argument equal to the result. Similarly, the `fn` macro also "cheats" away the set of parentheses that would be required around the functions arguments list by assuming the first non-symbol is the start of the function body. `fn` also avoids using "return" by assuming the last-evaluated expression is meant to be returned.

Note for Pythonists: There's a lot of behind-the-scenes magic at play with how `=` and `fn` work. The main difference between most languages and a Lisp like Pyylisp is that lots of the magic is implemented in the language itself, so people programming in the language can make their own magic.


## Separating things
Whitespace characters separate things. You don't use commas for this.


## Quoting
Pyylisp borrows from Common Lisp (and likely many other Lisps) these list operations:
* Quote: `'` causes something to be treated as data so it doesn't get interpreted. If applied to a list, this is applied recursively to everything inside the list.
* Backtick: `\`` causes a list to be quoted, but also allows for unquoting specific elements.
* Comma: `,` unquotes an item inside of a backticked list. This is useful for code templating in macros.
* Doublequotes: `"` begins and ends strings. These are much like other languages' strings, including backslash `\\` escapes inside of strings. Note, however, that Pyylisp strings can cover multiple lines.

## List expansion
Because `*` needs to be available as a symbol for multiplication, Pyylisp lists are expanded with `@` instead of Python's overloaded `*`. This matches Common Lisp.

For example, if you have a function `myfun` which takes 3 arguments you can do this
	= args list arg1 arg2 arg3
	myfun @args
and args will be expanded to call `myfun arg1 arg2 arg3`.


## Symbols
In Lisp terminology a "symbol" is essentially the name of a variable, function, or other thing. Unlike most programming languages, Pyylisp (and most any Lisp) lets you use pretty much any character you want in a symbol, as long as the character's not used for syntax. For example, instead of doAwesomeStuff, you can call your function do-awesome-stuff and avoid the Shift key.

Or, if you're feeling evil, you can define a symbol named -+*/^øØô²₃$%&! and bind a function or variable to it. However, you'll need to retype it exactly every time you call it.



# Data types
Pyylisp's data types mirror Python's. The main differences are that an uncompiled Pyylisp function is a list and that Pyylisp has macros as a special case of functions.


## Primitives
All the basic Python primitive data types are the same in Pyylisp. This includes:
* numbers
* strings
* booleans
* whatever might be missing from this list


## Ordered sequence types
Pyylisp lists are similar to Python's. Other than syntax changes below, any differences will be figured out during implementation. Here's how Pyylisp list access looks.

Get empty list:
* Pyylisp: `[]`, but it technically returns a function, making stuff more convenient later....
* Python: `[]`

Indexing:
* Pyylisp: `my-list i`
* Python: `myList[i]`

Setting index to value:
* Pyylisp: `my-list i new-value`
* Python: `myList[i] = newValue`

Getting slice from index i inclusive through index j exclusive:
* Pyylisp: `my-list i : j
* Python: `myList[i:]`

Replacing slice range with list:
* Pyylisp: `my-list i : j values`
* Python: `myList[i:j] = values`
* Note: In both of these cases `values` can be a symbol with a list bound to it or it can be a bunch of items like a list without the parentheses.

Skipping i or j in a slice:
* Pyylisp: `my-list :: j`, `my-list i ::`, or `my-list :::`
* Python: `myList[:j]`, `myList[i:]`, or `myList[:]`
* Note: In either Python or Pyylisp these can be followed by their respective slice-setting expressions.

Pyylisp might get separate array, tuple, and iterator types later. Basic lists are enough until after Pyylisp becomes a Lisp.


## Dictionaries
This works essentially the same as in Python, but with Pyylisp syntax. Here are some examples.

Make empty dictionary:
* Pyylisp: `{}`, but it technically returns a function, which is convenient later....
* Python: `{}`

Making a dictionary with three entries:
* Pyylisp: `{} key1 val1 key2 val2 key3 val3` and so on. You can also group the key-value pairs with parentheses or indentation. `{}` is smart enough to look inside if it sees a list where a key belongs.
* Python: `{key1:val1, key2:val2, key3:val3}` and so on.

Setting a key to a value:
* Pyylisp: `my-dict key value`
* Python: `myDict[key] = value`

Getting a key's value:
* Pyylisp: `my-dict key`
* Python: `myDict[key]`


## Functions
**UPDATE THIS**

Because doing things is the most common thing to do in a program, the default interpretation of a list is a function followed by its arguments. To use a list as data instead, precede it with a single quote like `'(this is a quoted list)`. Macros should be able to do fancy stuff to change this or something.


# Object-oriented stuff
**THIS SECTION NEEDS TO BE UPDATED TO MATCH THE MAGIC THAT THE `=` MACRO WILL DO**

I think that something like `. object field subfield` is the "right" way to retrieve what would be referred to as `object.field.subfield` and `. object method argument` is the way to do `object.method(argument)`. An object is just a templated dictionary with syntactic sugar, so it's not a big deal anyway.


## Python keywords and syntax
Everything you can do with Python keywords and syntax is available in Pyylisp. However, all that stuff has been turned into functions. For example, instead of

	for x in y:
		print(x)

you can say

	for-in x y
		print x

## Lisp macros
**ADD BASIC EXAMPLES**

I know that "macros" are meant to be like the holy grail of programming expressiveness power that turns every Lisp practitioner into a sanctified zealot or some such. However, I can't build them until I learn them. I'll probably write the Pyylisp macro system as soon as it seems like the most urgent/immediately-useful thing.

Note that half the Python I know is from searching for ways to avoid repeating myself in code. I expect that this is the force that will lead me to eventual understanding of Lisp macros.
