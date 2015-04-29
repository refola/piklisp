'''
chN.py TODO
Author: Mark Haferkamp
Last date modified: 2015-??-?? TODO

Homework template used with dry.py.
'''

chapter = ''# TODO

# Manually import chapter-specific dryN.py instead of dry.py because Canvas is /helpfully/ renaming everything that has the same name as a previously-submitted file.
dry = __import__('dry%s' % chapter)

import sys

# Functions for different problems, named via Lojban number words.
# TODO: After making Pyylisp, rewrite the current function skeletons stuff as a macro, something like this:
# (dry.add-fn fn-name "function description" arg1 str arg2 int)

# 1
def pa(*args):
	print("This sentence should describe the problem.")
	args = dry.getArgs(args, ("arg1", str), ("arg2", int))

# 3
def ci(*args):
	print("stuff")
	args = dry.getArgs(args, ("arg1", str))

# 5
def mu(*args):
	print("stuff")
	args = dry.getArgs(args, ("arg1", str))

# 7
def ze(*args):
	print("stuff")
	args = dry.getArgs(args, ("arg1", str))

# 9
def so(*args):
	print("stuff")
	args = dry.getArgs(args, ("arg1", str))

# Homework-specific usage function.
def usage(keys):
	print("Usage: python3 %s [n] [args]" % sys.argv[0])
	print("Does Chapter %s Project number n stuff, optionally with arguments replacing prompted-for stuff." % chapter)
	print("Implemented projects are as follows: %s" % keys)

def main():
	fmap = {"1":pa, "3":ci, "5":mu, "7":ze, "9":so}
	running=lambda name: "Running code for problem number %s." % name
	dry.runThings(fmap, fnPrompt="problem number", running=running, usage=usage)

main()
