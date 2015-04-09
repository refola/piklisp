#!/usr/bin/python3
'''
pyylisp.py
Author: Mark Haferkamp
Last date modified: 2015-04-08
Interpret a Pythony dialect of Lisp.

Pyylisp is a scripting language that uses a parentheses-light Lisp syntax and macro system to run Python functions.

It's essentially Pythonic syntax and features combined with Lisp semantics and listiness. As Clojure is to Java, Pyylisp tries to be to Python.
'''

import sys
import tokens
import parser
import compiler

def getLines(filename):
	'''Get the lines of text in a file, without line breaks.'''
	f = open(filename, 'rt')
	lines = list(l in f)
	return lines

def process(filename):
	'''Process a single file. Takse the name of a .pyl file and saves the result to a .py file.'''
	lineList = getLines(filename)
	tokenList = tokens.convert(lineList)
	parseTree = parser.parseTokens(tokenList)
	compiled = compiler.compileTree(parseTree)
	writeFile(compiled)

def usage():
	'''Show how to use the program.'''
	print("Usage: %s pyl-file-1 [pyl-file-2 [...]]" % sys.argv[0])
	print()
	print("Converts given .pyl Pyylisp files into .py Python files.")
	print("You probably want to run this as '%s *.pyl'." % sys.argv[0])

def main():
	'''Figure out what to do.'''
	args=sys.argv[1:]
	if len(args) == 0:
		usage()
		return
	for arg in args:
		if arg[-4:] != '.pyl':
			print("Invalid Pyylisp file: %s." % arg)
			usage()
			return
	for arg in args:
		process(arg)

main()
