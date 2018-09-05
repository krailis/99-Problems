# My attempt to solve the 99 PROLOG problems in Python
# This file includes solutions to problems 11 - 20

import sys
sys.path.insert(0, '../')
from p01_to_p10_solutions.solutions_1_10 import s9_packConsecutiveDuplicates 

# Problem 11: Modified Length Encoding of List
def s11_modifiedLengthEncoding (list_a):
	packList = s9_packConsecutiveDuplicates(list_a)
	encodedList = []
	for x in packList:
		if (len(x) > 1):
			encodedList.append([len(x), x[0]])
		else:
			encodedList.append(x[0])
	return encodedList

# Problem 12: Decode a run-length encoded list
def s12_decodeList (list_a):
	decodedList = []
	for x in list_a:
		if (isinstance(x, list)):
			decodedList.extend(x[0] * [x[1]])
		else:
			decodedList.append(x)
	return decodedList

# Problem 13: Run-length encoding of a list (direct solution)
def s13_directLengthEncoding (list_a):
	# Firstly find the list indexes that two subsequent elements differ
	indexOfChanges = [i for i, x in enumerate(list_a) if x != list_a[i - 1]]
	indexOfChanges.append(len(list_a))
	l = len(indexOfChanges)
	encodedList = []
	for i in range(1, l):
		# Subtract the indexes to find the plurality of a element
		count = indexOfChanges[i] - indexOfChanges[i - 1]
		if (count != 1):
			encodedList.append([count, list_a[indexOfChanges[i - 1]]])
		else:
			encodedList.append(list_a[indexOfChanges[i - 1]])
	return encodedList


# Problem 14: Duplicate the Elements of a list
def s14_duplicateListElements (list_a):
	duplicatedList = []
	for x in list_a:
		duplicatedList.extend([x, x])
	return duplicatedList

# Problem 15: Duplicate the elements of a list a given number of times
def s15_duplicateGivenTimes (list_a, n):
	duplicatedList = []
	for x in list_a:
		duplicatedList.extend(n * [x])
	return duplicatedList

# Problem 16: Drop every N'th element from a list
def s16_dropEveryNthElement (list_a, n):
	return [x for i, x in enumerate(list_a) if ((i + 1) % n != 0)]

# Problem 17: Split a list in two parts; the length of the first list is given
def s17_splitList (list_a, n):
	return [list_a[:n], list_a[n:]]

# Problem 18: Extract a slice from list
def s18_extractSlice (list_a, start, end):
	return list_a[(start - 1):(end - 1)]

# Problem 19: Rotate a List N places to the left
def s19_rotateList (list_a, n):
	rotatedList = list_a[n:]
	rotatedList.extend(list_a[:n])
	return rotatedList

# Problem 20: Remove K'th element from list
def s20_removeKthElement (list_a, k):
	retList = list_a[:(k-1)]
	retList.extend(list_a[k:])
	return retList

