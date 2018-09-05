# My attempt to solve the 99 PROLOG problems in Python
# This file includes solutions to problems 45 - 49

from re import finditer
import queue
import itertools

def NOT(a): return (not a)
def AND(a, b): return a and b
def OR(a, b): return a or b
def NAND(a, b): return not (a and b)
def NOR(a, b): return not (a or b)
def XOR(a, b): return a ^ b
def IMPL(a, b): return (not a) or b
def EQU(a, b): return not (a ^ b)

# Problem 45: Truth tables for logical expressions (prefix operators)
def s45_table (expr):
	print("%-5s %-5s %-5s" % ("A", "B", expr))
	for A in (True, False):
		for B in (True, False):
			# Convert to uppercase letters and evaluate expression using eval()
			print("%-5s %-5s %-5s" % (str(A), str(B), str(eval(expr.upper()))))

# Problem 46: Truth tables for logical expressions (infix operators)
def s46_tablePrefix (expr, ret = False):
	# Defining precedence of operations
	prec = { '(' : 0,
		 'impl' : 1, 'or' : 2,
		 'nor' : 3, 'xor' : 3,
		 'equ' : 3, 'and' : 4,
		 'nand' : 4, 'not' : 5}
	def infixToPostfix (expr):
		# An implementation of Dijkstra's Shunting Yard Algorithm
		# Details can be found on Wikipedia
		output = []
		opStack = []
		# Define a regular expression for matching expr
		# Matching parentheses, operators and operands A, B etc.
		regularExpression = r"([()])|(and|or|nand|nor|not|xor|equ|impl)|(\w+)"
		for paren, op, var in (matches.groups() for matches in finditer(regularExpression, expr)):
			if var is not None:
				output.append(var)
			if op is not None:
				while (opStack != [] and prec[op] <= prec[opStack[-1]]):
					output.append(opStack.pop())
				opStack.append(op)
			if (paren == '('):
				opStack.append(paren)
			elif (paren == ')'):
				while (opStack[-1] != '('):
					output.append(opStack.pop())
				opStack.pop()
		while (opStack != []):
			output.append(opStack.pop())
		return output
	
	# Function for postfix to prefix conversion
	def postfixToPrefix (exprPostfix):
		expr, nParen, notExists = "", 0, []
		while (exprPostfix != []):
			token = exprPostfix.pop()
			if (token in prec):
				if (token == 'not' and not(exprPostfix[-1] in prec)):
					expr += "not(" + exprPostfix.pop() + "),"
				elif (token == 'not' and exprPostfix[-1] in prec):
					expr += "not("
					notExists.append(")")
					nParen += 1
				else:
					if (expr != ""):
						if (expr[-1] == ')'):
							expr += "," + token + "("
						else:
							expr += token + "("
					else:
						expr += token + "("
					nParen += 1
			else:
				if (expr[-1] == '('):
					expr += token + ","
				elif (expr[-1] == ')'):
					if (notExists != []):
						expr += ")," + token + ")"
						notExists.pop()
						nParen -= 1
					else:
						expr += "," + token + ")"
					nParen -= 1
				else:
					expr += token + ")"
					nParen -= 1
		expr += nParen*")"
		return expr

	exprPostfix = infixToPostfix(expr)
	exprPrefix = postfixToPrefix(exprPostfix)
	if (ret):
		return exprPrefix

	print("%-5s %-5s %-5s" % ("A", "B", expr))
	for A in (True, False):
		for B in (True, False):
			# Convert to uppercase letters and evaluate expression using eval()
			print("%-5s %-5s %-5s" % (str(A), str(B), str(eval(exprPrefix.upper()))))

# Problem 47: Truth tables for logical expressions (infix operatots and arbitrary number of operands)
def s47_tableArbitrary (operands, expr):
	exprPrefix = s46_tablePrefix(expr, True)
	combos = list(itertools.product((True, False), repeat = len(operands)))
	outputFormat = (len(operands) + 1)*"%-5s "
	operands.append(expr)
	print(outputFormat % tuple(operands))
	operands.pop()
	for x in combos:
		y = list(x)
		for op in operands:
			exec(op + "=" + str(y.pop(0)))
		print(outputFormat % (x + (str(eval(exprPrefix.upper())),)))

# Problem 48: Gray Code
def s48_grayCode (n):
	if (n == 1):
		return ['0', '1']
	grayCode = ['0', '1']
	for i in range(0, n - 1):
		# Prefix list elements with '0'
		grayCodeLeft = ['0' + x for x in grayCode]
		grayCode.reverse()
		# After reversing prefix list elements with '1'
		grayCodeRight = ['1' + x for x in grayCode]
		# Join lists
		grayCodeLeft.extend(grayCodeRight)
		grayCode = grayCodeLeft
	return grayCode

# Problem 49: Huffman Code
def s49_huffman (Fs):
	# A definition of a tree node
	class treeNode(object):
		def __init__(self, left = None, right = None, root = None):
			self.left = left
			self.right = right
			self.root = root
		def children(self):
			return ((self.left, self.right))
	
	# A function for creating a tree according to Huffman coding alorithm
	def create_tree (freqs):
		priorityQueue = queue.PriorityQueue()
		for x in freqs:
			priorityQueue.put(x)
		while priorityQueue.qsize() > 1:
			left = priorityQueue.get()
			right = priorityQueue.get()
			node = treeNode(left, right)
			priorityQueue.put((left[0] + right[0], node))
		return priorityQueue.get()
	
	# A function for walking the tree
	def treeWalk(node, prefix = "", code = []):
		if (isinstance(node[1].left[1], str)):
			code.append((node[1].left[1], prefix + "0"))
		else:
			code = treeWalk(node[1].left, prefix + "0", code)
		if (isinstance(node[1].right[1], str)):
			code.append((node[1].right[1], prefix + "1"))
		else:
			code = treeWalk(node[1].right, prefix + "1", code)
		return code

	root = create_tree(Fs)
	code = treeWalk(root)
	return sorted(code)
