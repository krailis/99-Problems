# My attempt to solve the 99 PROLOG problems in python
# This file includes solutions to problems 21 - 28

import random
import itertools

# Problem 21: Insert element at a given position into a list
def s21_insertElement (list_a, n, item):
	list_a.insert(n - 1, item)
	return list_a

# Problem 22: Create a list containing all integers within a given range
def s22_range (start, end):
	return list(range(start, end + 1))

# Problem 23: Extract a given number of randomly selected items from a list
def s23_extractRandom (list_a, n):
	return random.sample(list_a, n)

# Problem 24: Lotto; Draw N different random numbers from the set 1..M
def s24_lotto (n, m):
	return s23_extractRandom(s22_range(1, m), n)

# Problem 25: Generate Random Permutation of List
def s25_randomPermutation (list_a):
	return s23_extractRandom(list_a, len(list_a))

# Problem 26: Generate the combinations of K distinct objects chosen from N elements of list
def s26_combinations (K, list_a):
	return list(itertools.combinations(list_a, K))

# Problem 27: Group elements of set into disjoint subsets
def s27_disjointSubsets (list_a, groups):
	set_a = set(list_a)
	# Find all combinations with the given plurality of the first subset
	firstSet = itertools.combinations(set_a, groups[0])
	disjointList = []
	for x in firstSet:
		# For every subset of the possible combinations of the first
		# group, remove its members and find all combinations with
		# given plurality of the second subset
		tempSubset = set_a - set(x)
		secondSet = itertools.combinations(tempSubset, groups[1])
		list_x = list(x)
		for y in secondSet:
			subset = [list_x, list(y)]
			# Finally append the remaining elements to the end
			subset.append(list(tempSubset - set(y)))
			disjointList.append(subset)
	return disjointList

# Problem 28: Sort lists according to length of sublists
def s28_sortLists_a (list_a):
	indexLength = []
	sortedList = []
	for i, x in enumerate(list_a):
		indexLength.append([len(x), i])
	indexLength.sort();
	for x in indexLength:
		sortedList.append(list_a[x[-1]])
	return sortedList

def s28_sortLists_b (list_a):
	listLengths = set(map(len, list_a))
	sortedList = []
	indexLengthCounts = []
	for x in listLengths:
		specificLengthList = [y for y in list_a if len(y) == x]
		indexLengthCounts.append(specificLengthList)
	lengthSorted = sorted(indexLengthCounts, key = len)
	for x in lengthSorted:
		sortedList.extend(x)
	return sortedList
