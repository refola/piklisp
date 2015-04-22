'''
tokenize.py
Author: Mark Haferkamp
Last modified: 2015-04-08

Convert a bunch of text into Piklisp tokens.
'''

class Token(object):
	"""Representation of a single token in a parse of a Piklisp file."""

	# Types of token
	GROUPING = "grouping"
	LIST_OPERATION = "list operation"
	QUOTE = "quote"
	COMMENT = "comment"
	SYMBOL = "symbol"

	def __init__(self, _type, content):
		self._type = _type
		self.content = content

# Grouping tokens, the thing that Lisp parentheses and Python indentation means. Content is given as parentheses to be lazy; outputted .py code doesn't have to look pretty.
START_GROUP = Token(Token.GROUPING, '(')
END_GROUP = Token(Token.GROUPING, ')')

def indentLevel(line):
	"""Returns the indentation level of a line, defined in Piklisp as the number of leading tabs."""
	for i in range(len(line)):
		if line[i] != "\t":
			return i # i characters were "\t" before lines[i]
	return None # only whitespace -> nothing is indented

def convert(lines):
	"""Iterates over an iterable of lines (e.g., a file object in text mode) and returns a list of tokens."""
	indentLevel = 0 # The level of indentation we're at, necessary for inferring parentheses from indentation
	tokens = []
	prevLineStart = 0 # Index of previous line's start, for inserting indentation-based START_GROUP tokens when the indentation level increases.
	def insertIndentStarts(n):
		for i in range(n):
			tokens.insert(prevLineStart, START_GROUP)
	for line in lines:
		newPrevLineStart = len(tokens)
		line = line[:-1] # strip trailing '\n'; we're after the lines, not the separators between them
		if not hasContent(line):
			continue # skip blank or comment-only lines
		i = indentLevel(line)
		if i == None:
			continue 
		deltaIndent = i - indentLevel
		if deltaIndent > 0:
			insertIndentStarts(deltaIndent)
		prevLineStart = newPrevLineStart

