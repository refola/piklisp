'''
dry.py

Tools to help you avoid repeating yourself. This does not quite match
the Piklisp because normal Python can't do macros, which are used for
"seval" and "sevals".
'''

# Commented out because it doesn't work on Windows. :-(
#import readline # Make input() provide fancy line editing and history.
import sys


### Utility functions

## Here are some functions for evaluating stuff and showing the expression being evaluated. This would be useful if it could work like Lisp macros, but in Python this sort of thing needs to be manually copied into every scope it's used in.
# Throw away the value when using lambdas for function invocations.
null = lambda *_: None
# Show and EVAL a string. Yay lambdas!
seval = lambda x: print("%20s == %r" % (x, eval(x))) # Converting this into a function that passes the lambda doesn't fix scope issues.
# Run seval on everything. Yay list comprehensions!
sevals = lambda *things: null([seval(thing) for thing in things])

# Pause until the user presses enter, allowing the program to do the following action.
def pause(action="continue"): input("Press [Enter] to %s. " % action)


### Get arguments of the correct type, prompting the user as necessary.

# Attempt conversion of value to Type.
def tryConvert(value, Type):
	try:
		return Type(value)
	except ValueError:
		return None

# Get input by type, looping until satisfied.
def getByType(name, Type):
	ret = None
	while ret is None:
		ret = tryConvert(input("Please enter %s. " % name), Type)
		if ret is None:
			print("Error. I was expecting input of type %s." % Type)
	return ret

# Get arguments interactively if full args list not given. Descriptions are 2-tuples containing the text to show the user and the type of thing you want. Use getByType to get a single argument.
def getArgs(given, *descriptions):
	ret = []
	# First try seeing if the arguments work.
	if len(given) == len(descriptions):
		types = map(lambda x:x[1], descriptions)
		valTypePairs = zip(given, types)
		ret = tuple(tryConvert(*x) for x in valTypePairs)
		if not None in ret: # If all conversions successful
			return ret
	# If not, get fresh input.
	return [getByType(*desc) for desc in descriptions]


### Run functions with a minimal menu list.

# Tell the user what functions are available.
def defaultusage(keys):
	print("Usage: python3 %s [fn] [args]" % sys.argv[0])
	print("Runs function fn, optionally with given arguments.")
	print("Functions are as follows: %s" % keys)

# Call the appropriate function, prompting the user if one isn't specified.
def runThings(fmap, *, args=sys.argv[1:], fnPrompt="function name", running=lambda name:"Running function %s."%name, usage=defaultusage):
	# Report if the given function could be ran.
	def tryRun(fn, args):
		if fn in fmap:
			print(running(fn))
			fmap[fn](*args)
			return True
		else:
			print("Invalid %s: '%s'." % (fnPrompt, fn))
			return False
	# Keys for usage function's reference
	keys = list(fmap.keys())
	keys.sort()
	# Until function invoked, prompt for function name
	while len(args) < 1 or not tryRun(args[0], args[1:]):
		usage(keys)
		args=[getByType(fnPrompt, str)]
