# My attempt to solve the 99 PROLOG problems in Python
# This file includes solutions to problems 1 - 10

# Problem 1: Find The Last Element of a List
def s1_lastElement (list_a):
	return list_a[-1]

# Problem 2: Find the Last but One Element of a List
def s2_lastButOne (list_a):
	return list_a[-2]

# Problem 3: Find the K'th Element of a List
def s3_kthElement (list_a, k):
	return list_a[k-1]

# Problem 4: Find the number of Elements of a List
def s4_listLength (list_a):
	return len(list_a)

# Problem 5: Reverse a List
def s5_listReverse (list_a):
	list_a.reverse()
	return list_a

# Problem 6: Find out whether a list is palindrome
def s6_isPalindrome (list_a):
	l = int(len(list_a)/2)
	# Compare elements of the list symmetrically. If any two symmetric elements
	# differ then the list is not palindrome
	for i in range(0, l):
		if (list_a[i] != list_a[-1-i]):
			return False
	return True

# Problem 7: Flatten a Nested List Structure
def s7_flattenList (list_a):
	flat = []
	for x in list_a:
		# If element x is a list then the initial list should be extended
		# by the elements of list x
		if (isinstance(x, list)):
			flat.extend(s7_flattenList(x))
		# otherwise a single element is appended
		else:
			flat.append(x)
	
	return flat

# Problem 8: Eliminate Consecutive Duplicates of List
# First solution: Use of 'enumerate' offered by python
def s8_eliminateConsecutiveDuplicates_1 (list_a):
	return [x for i, x in enumerate(list_a) if x != list_a[i-1]]

# Second Solution: More Custom Solution	
def s8_eliminateConsecutiveDuplicates_2 (list_a):
	b = list(range(0, len(list_a)))
	c = []
	# Creating an enumerated list in order to have indexing of the list elements
	for x in list_a:
		c.append((x, b.pop(0)))
	return [x for (x, y) in c if x != list_a[y-1]]

# Problem 9: Pack Consecutive Duplicates of a List
def s9_packConsecutiveDuplicates (list_a):
	packList = []
	subList = []
	l = len(list_a)-1
	while True:
		# Pop the first element of input list at every iteration
		# and append it to the sublist
		x = list_a.pop(0)
		subList.append(x)
		if (list_a != []):
			# As long as the input list is not empty compare
			# the popped element with the new first element
			if (x != list_a[0]):
				packList.append(subList)
				subList = []
		else:
			packList.append(subList)
			break
	
	return packList		

# Problem 10: Run Length Encoding of List
def s10_listLengthEncoding (list_a):
	packList = s9_packConsecutiveDuplicates(list_a)
	encodedList = []
	# After packing the list using the previous function use the
	# sublist length and append the new pair to the output list
	for x in packList:
		encodedList.append([len(x), x[0]])
	return encodedList
